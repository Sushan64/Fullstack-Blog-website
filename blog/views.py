from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def index(request):
  #All Post
  posts = Post.objects.all().order_by('-published_date')
  p = Paginator(posts, 2)
  page_number = request.GET.get('page')
  page_obj = p.get_page(page_number)

  #Tech
  tech = Post.objects.filter(category='Tech').order_by('-published_date')
  
  context={
    "posts": posts,
    "page_obj": page_obj,
    "tech": tech
  }
  
  return render(request, "blog/index.html", context)



def post(request, pk):
  post = get_object_or_404(Post, pk=pk)
  relateds = Post.objects.filter(category=post.category).exclude(pk=post.pk).order_by('-published_date')[:5]
  
  return render(request, "blog/post.html", {"post": post, "relateds": relateds})



def category(request, category_value):
  category_post = Post.objects.filter(category=category_value).order_by('-published_date')

  p = Paginator(category_post, 5)
  page_number = request.GET.get('page')
  page_obj = p.get_page(page_number)
  
  return render(request, "blog/category.html", {
    "category_post": category_post,
    "category_value": category_value,
    "page_obj": page_obj
  })