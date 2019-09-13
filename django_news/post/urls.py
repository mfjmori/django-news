from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_index, name='post_index'),
  path('new/', views.post_new, name='post_new'),
  path('show/<int:pk>', views.post_show, name='post_show'),
]
