"""Forms for the blog."""

from django import forms


class EmailPostForm(forms.Form):
    """Form for sending articles by email."""

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
