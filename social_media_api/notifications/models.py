from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    # The user who will receive the notification
    recipient = models.ForeignKey(User, related_name="notifications", on_delete=models.CASCADE)

    # The user who triggered the notification (actor)
    actor = models.ForeignKey(User, related_name="generated_notifications", on_delete=models.CASCADE)

    # The verb describes the action taken by the actor (e.g., 'liked', 'followed', 'commented')
    verb = models.CharField(max_length=255)

    # The target is a GenericForeignKey to allow notification for different models (e.g., Post, Comment)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    # Timestamp when the notification was created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target} for {self.recipient}
