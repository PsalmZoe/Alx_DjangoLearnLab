from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Optional: Create a simple home view
def home_view(request):
    return HttpResponse("<h1>Welcome to the Library App!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # Include app URLs
    path('', home_view, name='home'),  # Root URL pattern
]
