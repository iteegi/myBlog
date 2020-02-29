"""Views for the blog."""

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    """Process the request to display a list of articles."""
    object_list = Post.published.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, return the first page.
        posts = paginator.page(1)
    except EmptyPage:
        """ If the page number is greater than the total number of pages,
        return the last."""
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts})


def post_detail(request, year, month, day, post):
    """Process the request to display the article page."""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
