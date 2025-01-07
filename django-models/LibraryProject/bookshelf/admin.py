from django.contrib import admin
from .models import Book

@admin.register(Book)  # This is a decorator to register the model with a custom admin class
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Filters for narrowing down the list
    list_filter = ('publication_year',)

    # Search functionality
    search_fields = ('title', 'author')
