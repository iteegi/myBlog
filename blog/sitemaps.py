"""Sitemap."""

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """Own site map object."""

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        """Return a QuerySet of objects to be displayed in site map."""
        return Post.published.all()

    def lastmod(self, obj):
        """Return time of last modification of article."""
        return obj.updated
