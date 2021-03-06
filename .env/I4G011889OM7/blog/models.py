from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=200)
    Author = models.ForeignKey(User, blank=True)
    Created_date = models.DateTimeField(auto_now=True)
    Published_date = models.DateTimeField(auto_now=True)