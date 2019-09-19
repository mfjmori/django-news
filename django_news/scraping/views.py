from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Scraping

def scraping_index(request):
  scrapings = Scraping.objects.order_by('publish_at').reverse()
  page = Paginator(scrapings, 25)
  if request.GET.get('p'):
    num = int(request.GET.get('p'))
  else:
    num = None

  params = {
      'articles': page.get_page(num),
      'page': page.page_range,
      'page_active': num,
      'page_last': page.num_pages
    }
  return render(request, 'scraping/scraping_index.html', params )
