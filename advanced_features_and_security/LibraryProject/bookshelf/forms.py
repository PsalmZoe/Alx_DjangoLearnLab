from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    # You can add additional custom validation if needed
    def clean_title(self):
        title = self.cleaned_data['title']
        # You could add custom title validation here, like checking length or disallowing certain words.
        return title
