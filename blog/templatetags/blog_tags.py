"""Custom tags for the blog."""

from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Return the number of published articles."""
    return Post.published.count()
