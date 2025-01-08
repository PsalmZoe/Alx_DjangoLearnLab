from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    context = {'books': books}
    return render(request, 'list_books.html', context)

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)  # Explicit path

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Explicit path
    context_object_name = 'library'

from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Custom registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})