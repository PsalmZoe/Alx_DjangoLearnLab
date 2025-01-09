from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Post

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

User = get_user_model()

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)

    # Use a string reference for the Post model to avoid circular imports
    post = models.ForeignKey('Post', related_name="likes", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Ensure a user can like a post only once

    def __str__(self):
        return f'{self.user.username} liked {self.post.title}'
