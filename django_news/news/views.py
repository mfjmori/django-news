from django.shortcuts import render, redirect
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
