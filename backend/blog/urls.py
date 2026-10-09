from django.urls import path
from .views import (AllBlogPostsAPIView, CategoryAPIView, BlogPostAPIView, BlogPostCreateAPIView, CategoryListView,
                    PostListCreateView, PostDetailView, RelatedPostsView, LikeView,
                    CommentListCreateView, CommentDeleteView, ContactView, RegisterView, MeView)

urlpatterns = [
    path('categories/search/', CategoryAPIView.as_view(), name='category-detail'),
    path('posts/search/', BlogPostAPIView.as_view(), name='blog-post-detail'),
    path('all-posts/', AllBlogPostsAPIView.as_view(), name='all-posts'),
    path('posts/create/', BlogPostCreateAPIView.as_view(), name='blog-post-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    # Editorial API (additive)
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<slug:slug>/related/', RelatedPostsView.as_view(), name='post-related'),
    path('posts/<slug:slug>/like/', LikeView.as_view(), name='post-like'),
    path('posts/<slug:slug>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('comments/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/me/', MeView.as_view(), name='me'),
]
