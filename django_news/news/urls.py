from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
  path('', RedirectView.as_view(url='business')),
  path('<str>/', views.news_index, name='news_index'),
]
