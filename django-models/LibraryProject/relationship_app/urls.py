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
