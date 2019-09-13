from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_index(request):
  posts = Post.objects.all().order_by('publish_at').reverse
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

@login_required
def post_show(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'post/post_show.html', {'post': post})
