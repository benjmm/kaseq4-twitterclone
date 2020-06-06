from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=50, unique=True)
    following = models.ManyToManyField(
        'self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
