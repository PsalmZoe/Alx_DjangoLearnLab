# delete.md
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()  # Expected Output: <QuerySet []
from bookshelf.models import Book