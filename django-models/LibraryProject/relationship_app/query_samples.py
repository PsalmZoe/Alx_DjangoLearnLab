from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using objects.filter()
        for book in books:
            print(f"{book.title} by {book.author.name}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToManyField
        for book in books:
            print(f"{book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOneField
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'.")

# Example usage
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    books_in_library("City Library")
    librarian_for_library("City Library")
