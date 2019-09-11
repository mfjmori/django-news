from django.shortcuts import render
import requests, os

def news_index(request):
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  NEWS_API_URL = os.environ.get('NEWS_API_URL')
  response_res = requests.get(NEWS_API_URL, {'country' : 'jp', 'category': 'business', 'apiKey' : NEWS_API_KEY})
  response_dict = response_res.json()
  return render(request, 'news/news_index.html', { 'articles' : response_dict['articles']})
