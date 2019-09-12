from django.db import models
from django.utils import timezone

class Stock(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  url = models.URLField()
  image_url = models.URLField(null=True, blank=True)
  title = models.CharField(max_length=100)
  body = models.TextField(null=True, blank=True)
  source = models.CharField(null=True, max_length=50)
  likes_count = models.IntegerField(null=True, blank=True)
  publish_at = models.DateTimeField()

  class Meta:
    unique_together = ['user', 'url']
