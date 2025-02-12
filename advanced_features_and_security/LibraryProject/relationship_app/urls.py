from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    # Authentication URLs
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
