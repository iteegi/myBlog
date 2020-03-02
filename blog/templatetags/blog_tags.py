"""Custom tags for the blog."""

from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Return the number of published articles."""
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """Return the last few posts."""
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
