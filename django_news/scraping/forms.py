from django import forms
from .models import Scraping

class ScrapingForm(forms.ModelForm):

  class Meta:
    model = Scraping
    fields = ('title', 'body', 'image', 'publish_at', 'url')
