from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    authors = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 80, 'rows': 1, 'style': 'resize: none;'}),
        help_text="Enter author(s) separated by commas"
    )

class AuthorForm(forms.Form):
    name = forms.CharField(label='Author Name', max_length=100)