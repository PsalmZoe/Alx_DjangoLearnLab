from rest_framework import permissions, generics
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # Return the notifications for the authenticated user
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')
