from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="home"),
  path('post/<int:pk>/', views.post, name="post"),
  path('category/<str:category_value>/', views.category, name="category"),
]