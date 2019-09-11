from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('news_index', kwargs={'str': 'business'})
  template_name = 'accounts/signup.html'

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    self.object = user
    return redirect(self.get_success_url())
