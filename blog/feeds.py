"""RSS."""
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    """RSS model."""

    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        """Get objects to be included in the newsletter."""
        return Post.published.all()[:5]

    def item_title(self, item):
        """Get the title."""
        return item.title

    def item_description(self, item):
        """Get a description."""
        return truncatewords(item.body, 30)
