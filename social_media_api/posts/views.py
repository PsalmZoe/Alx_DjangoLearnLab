from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView
from notifications.models import Notification
from django.contrib.auth import get_user_model

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
