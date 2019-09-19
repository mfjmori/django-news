from django.shortcuts import render
from .models import Scraping

def scraping_index(request):
  Scrapings = Scraping.objects.order_by('publish_at').reverse()
  return render(request, 'scraping/scraping_index.html', {'articles' : Scrapings})
