from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.decorators import api_view

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Filter posts based on user
        return self.queryset.filter(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Filter comments based on user
        return self.queryset.filter(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# posts/views.py

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get posts from the users the current user is following
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

User = get_user_model()

class LikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Prevent the user from liking the post again
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a like
        like = Like.objects.create(user=user, post=post)

        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked",
            target=post
        )

        return Response({'detail': 'Post liked successfully'}, status=status.HTTP_201_CREATED)

class UnlikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Ensure the like exists before unliking
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()

            # Create a notification for unliking (optional)
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="unliked",
                target=post
            )

            return Response({'detail': 'Post unliked successfully'}, status=status.HTTP_200_OK)

        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

# posts/views.py

@api_view(['POST'])
def like_post(request, pk):
    # Get the post object or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)

    # Create or get the Like object for the current user and post
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        # If the like is created, return a success response
        return Response({"message": "Post liked successfully"}, status=status.HTTP_201_CREATED)
    else:
        # If the like already exists, return a response indicating the like already exists
        return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def unlike_post(request, pk):
    # Get the post object or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)

    try:
        # Try to find the existing Like object
        like = Like.objects.get(user=request.user, post=post)
        like.delete()  # Delete the like if it exists
        return Response({"message": "Post unliked successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        # If the like does not exist, return an error response
        return Response({"message": "You have not liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
