from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='posts', editable=False)
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
#        return reverse()
