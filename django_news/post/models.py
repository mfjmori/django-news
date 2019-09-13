from django.db import models
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  body = models.TextField()
  publish_at = models.DateTimeField()
