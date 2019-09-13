from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_index(request):
  posts = Post.objects.select_related('author').all().order_by('publish_at').reverse
  return render(request, 'post/post_index.html', {'posts' : posts})

@login_required
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      now = timezone.datetime.now()
      post.author = request.user
      post.publish_at = now
      post.save()
      return redirect('post_show', pk=post.pk )
  else:
    form = PostForm()
  return render(request, 'post/post_new.html', {'form': form} )

def post_show(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'post/post_show.html', {'post': post})

@login_required
def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST' and post.pk == request.user.id:
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      now = timezone.datetime.now()
      post.author = request.user
      post.publish_at = now
      post.save()
      return redirect('post_show', pk=pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'post/post_edit.html', { 'form' : form } )

@login_required
@require_POST
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if post.author.id == request.user.id:
    post.delete()
  return redirect('post_index')
