from django.shortcuts import render

# Create your views here.

# create.md
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected Output: <Book: 1984 by George Orwell (1949)>

# retrieve.md
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
