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

    from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_of_birth', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
        }),
    )
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)

