from django.db import models

class Scraping(models.Model):
  title = models.CharField(max_length=50)
  body = models.TextField()
  image = models.ImageField(upload_to='images', null=True, blank=True)
  publish_at = models.DateTimeField()
  url = models.URLField(unique=True)
