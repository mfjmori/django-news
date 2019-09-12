from django import forms
from django.shortcuts import redirect
from .models import Stock

class StockForm(forms.ModelForm):

  class Meta:
    model = Stock
    fields = ('url', 'image_url', 'title', 'body', 'source', 'likes_count', 'publish_at', 'user')

  def clean(self):
    cleaned_data = self.cleaned_data
    try:
      Stock.objects.get(url=cleaned_data['url'], user=cleaned_data['user'])
    except Stock.DoesNotExist:
      pass
    else:
      raise forms.ValidationError('Stock with this url already exists for this user')
      return cleaned_data
