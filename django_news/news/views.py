from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Stock
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
  if request.user.is_authenticated:
    urls = list(Stock.objects.filter(user_id=request.user.id).values_list('url', flat=True))
    return render(request, 'news/news_index.html', { 'articles' : response_dict['articles'], 'urls' : urls})
  else:
    return render(request, 'news/news_index.html', { 'articles' : response_dict['articles']})

def qiita_index(request):
  QIITA_API_URL = os.environ.get('QIITA_API_URL')
  response_res = requests.get(QIITA_API_URL, { 'page' : 1, 'per_page' : 20, 'query' : 'stocks:>20' })
  response_list = response_res.json()
  if request.user.is_authenticated:
    urls = list(Stock.objects.filter(user_id=request.user.id).values_list('url', flat=True))
    return render(request, 'news/qiita_index.html', { 'articles' : response_list, 'urls' : urls})
  else:
    return render(request, 'news/qiita_index.html', { 'articles' : response_list ,'urls' : urls})

@login_required
@require_POST
def stock_create(request):
  form = StockForm(request.POST)
  if form.is_valid():
    stock = form.save()
    messages.success(request, 'ストックしました')
  else:
    messages.error(request, 'ストックできませんでした')
  return redirect('news_index', str='business')

@login_required
def stock_index(request):
  stocks = Stock.objects.filter(user_id=request.user.id)
  return render(request, 'news/stock_index.html', { 'articles' : stocks } )

@login_required
@require_POST
def stock_delete(request, pk):
  stock = get_object_or_404(Stock, pk=pk)
  if stock.user_id == request.user.id:
    stock.delete()
    messages.success(request, '削除しました')
  else:
    messages.error(request, '不正なアクセスです')
  return redirect('stock_index')
