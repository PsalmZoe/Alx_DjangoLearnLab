from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet
from .views import LikePostAPIView, UnlikePostAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'feed', FeedViewSet, basename='feed')

urlpatterns = [
    path('feed/', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='unlike_post'),
]
