from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)

    def clean_title(self):
        title = self.cleaned_data['title']
        # Perform custom validation if necessary
        return title
