"""Custom tags for the blog."""

from django.db.models import Count
from django import template
from ..models import Post
from django.utils.safestring import mark_safe

import markdown

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


@register.simple_tag
def get_most_commented_posts(count=5):
    """Get the article with the most comments."""
    return Post.published.annotate(total_comments=Count('comments'))\
        .order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    """Populate article body with Markdown formatting."""
    return mark_safe(markdown.markdown(text))
