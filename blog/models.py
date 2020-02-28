"""BD models for the blog."""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """This is the data model for blog articles."""

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        """Meta data for post class.

        Default article sort order.
        Descending date of publication, publish field.

        """

        ordering = ('-publish',)

        def __str__(self):
            """Overwrite class name for the admin panel."""
            return self.title
