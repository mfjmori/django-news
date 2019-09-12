from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import StockForm
from . import urls
import requests, os

def news_index(request, str):
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  NEWS_API_URL = os.environ.get('NEWS_API_URL')
  categories = ['', 'business', 'science', 'technology']
  if str in categories:
    category = str
  else:
    return redirect('news_index', str='business')
  response_res = requests.get(NEWS_API_URL, {'country' : 'jp', 'category': category, 'apiKey' : NEWS_API_KEY})
  response_dict = response_res.json()
  return render(request, 'news/news_index.html', { 'articles' : response_dict['articles']})

@login_required
@require_POST
def news_create(request):
  form = StockForm(request.POST)
  if form.is_valid():
    stock = form.save()
  return redirect('news_index', str='business')
