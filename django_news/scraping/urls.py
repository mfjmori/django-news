from django.urls import path
from . import views

urlpatterns = [
  path('', views.scraping_index, name='scraping_index'),
]
