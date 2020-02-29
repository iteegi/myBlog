"""Views for the blog."""

from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """Process the request to display a list of articles."""
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    """Process the request to display the article page."""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
