"""Forms for the blog."""

from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    """Form for sending articles by email."""

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Form for sending comment."""

    class Meta:
        """Meta information for the CommentForm class."""

        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    """Form for the search."""

    query = forms.CharField()
