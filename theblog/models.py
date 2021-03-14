from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Model for blog posts"""
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
