from django.shortcuts import render

# Create your views here.

# create.md
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected Output: <Book: 1984 by George Orwell (1949)>

# read.md
book = Book.objects.get(title="1984")
book.title  # Expected Output: '1984'
book.author  # Expected Output: 'George Orwell'
book.publication_year  # Expected Output: 1949

# update.md
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title  # Expected Output: 'Nineteen Eighty-Four'

# delete.md
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()  # Expected Output: <QuerySet []>

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('articles.can_view', raise_exception=True)
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'view_article.html', {'article': article})

@permission_required('articles.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        # Handle the form submission and save the article
        pass
    return render(request, 'edit_article.html', {'article': article})

@permission_required('articles.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # Handle form submission and create the article
        pass
    return render(request, 'create_article.html')
