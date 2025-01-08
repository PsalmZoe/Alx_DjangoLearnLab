from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]

urlpatterns = [
    # Authentication routes
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Path for adding a book
    path('add-book/', views.add_book, name='add_book'),

    # Path for editing a book
    path('edit-book/<int:pk>/', views.edit_book, name='edit_book'),

    # Path for deleting a book
    path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),

    # Other URLs can go here
]

add-book /
edit-book/