from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def index(request):
  posts = Post.objects.all().order_by('-published_date')
  
  p = Paginator(posts, 1)
  page_number = request.GET.get('page')
  page_obj = p.get_page(page_number)
  
  return render(request, "blog/index.html", {"posts": posts, "page_obj": page_obj})

def post(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, "blog/post.html", {"post": post})