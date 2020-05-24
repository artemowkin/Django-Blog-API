from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


class NotSubcommentsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(author=None)


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='posts', blank=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='comments', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:15]
