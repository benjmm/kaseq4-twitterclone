from django.db import models
from django.utils import timezone
from twitteruser.models import CustomUser


class Tweet(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    body = models.TextField(max_length=140)
