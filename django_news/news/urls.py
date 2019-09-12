from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
  path('', RedirectView.as_view(url='business')),
  path('stocks/', views.stock_index, name='stock_index'),
  path('stock/create/', views.stock_create, name='stock_create'),
  path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
  path('<str>/', views.news_index, name='news_index'),
]
