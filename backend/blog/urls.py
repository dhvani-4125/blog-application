from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
    CommentDetailView,
    FeedbackListCreateView,
    FeedbackDetailView,
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('comments/',CommentListCreateView.as_view()),
    path('comments/<int:pk>/',CommentDetailView.as_view()),
    path('feedback/',FeedbackListCreateView.as_view()),
    path('feedback/<int:pk>/',FeedbackDetailView.as_view()),
]