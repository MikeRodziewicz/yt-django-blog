from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    """Model for blog posts"""
    title = models.CharField(max_length=256)
    title_tag = models.CharField(max_length=256, default="My Blog Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog-detail', args=(str(self.id)))