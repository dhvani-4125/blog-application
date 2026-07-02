from django.urls import path
from .views import (AllBlogPostsAPIView, CategoryAPIView,BlogPostAPIView, BlogPostCreateAPIView, CategoryListView)

urlpatterns = [
    path('categories/search/', CategoryAPIView.as_view(), name='category-detail'),
    path('posts/search/', BlogPostAPIView.as_view(), name='blog-post-detail'),
    path('all-posts/', AllBlogPostsAPIView.as_view(), name='all-posts'),
    path('posts/create/', BlogPostCreateAPIView.as_view(), name='blog-post-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
