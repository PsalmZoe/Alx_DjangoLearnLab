from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # Include the app's URLs
]
from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    # Authentication URLs
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegisterView  # Import the register view

urlpatterns = [
    # Login
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # Logout
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Register
    path('register/', UserRegisterView.as_view(), name='register'),
]

