# Django Admin Integration for Book Model

## Steps to Register and Customize the Admin Interface

### 1. Register the `Book` Model
- Open `bookshelf/admin.py`.
- Import the `Book` model: `from .models import Book`.
- Register the model: `admin.site.register(Book)`.

### 2. Customize the Admin Interface
- Replace the default registration with a custom admin class:
  ```python
  @admin.register(Book)
  class BookAdmin(admin.ModelAdmin):
      list_display = ('title', 'author', 'publication_year')
      list_filter = ('publication_year',)
      search_fields = ('title', 'author')
