from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class IssueBook(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.CharField(max_length=100)
    received = models.BooleanField()
