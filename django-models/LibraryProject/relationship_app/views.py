from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Login View
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after registration
