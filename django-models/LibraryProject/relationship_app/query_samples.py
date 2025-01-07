from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Using the related_name 'books'
    for book in books:
        print(f"{book.title} by {book.author.name}")

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # ManyToManyField
    for book in books:
        print(f"{book.title}")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # OneToOneField
    print(f"Librarian for {library.name}: {librarian.name}")

# Example usage
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    books_in_library("City Library")
    librarian_for_library("City Library")
