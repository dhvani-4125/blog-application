from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import Category, BlogPost, Comment, Feedback
from .serializers import CategorySerializer, BlogPostSerializer, CommentSerializer, FeedbackSerializer
from .utils import custom_response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .pagination import BlogPagination

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)

        return custom_response(success=True, message="Categories fetched successfully", data=serializer.data, status_code=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(success=True, message="Category created successfully", data=serializer.data, status_code=status.HTTP_201_CREATED)
        return custom_response(success=False, message="Failed to create category", errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return custom_response(success=True, message="Category fetched successfully", data=serializer.data, status_code=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.get-serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(success=True, message="Category updated successfully", data=serializer.data, status_code=status.HTTP_200_OK)
        return custom_response(success=False, message="Failed to update category", errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        category=self.get_object()
        category.delete()
        return custom_response(success=True, message="Category deleted successfully", status_code=status.HTTP_204_NO_CONTENT)

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    pagination_class = BlogPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ['category', 'status']

    search_fields = [
        'title',
        'content'
    ]

    ordering_fields = [
        'created_at',
        'title'
    ]

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(
            self.get_queryset()
        )

        page = self.paginate_queryset(queryset)

        if page is not None:

            serializer = self.get_serializer(
                page,
                many=True
            )

            return self.get_paginated_response(
                serializer.data
            )

        serializer = self.get_serializer(
            queryset,
            many=True
        )

        return custom_response(
            success=True,
            message="Posts fetched successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return custom_response(success=True, message="Post created successfully", data=serializer.data, status_code=status.HTTP_201_CREATED)
        
        return custom_response(success=False, message="Validation failed", errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
    
class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object()
        )

        return custom_response(success=True, message="Post fetched successfully", data=serializer.data, status_code=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object(),
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return custom_response(success=True, message="Post update successfully", data=serializer.data, status_code=status.HTTP_200_OK)
        
        return custom_response(success=False, message="Validation failed", errors=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return custom_response(success=True, message="Post deleted successfully", status_code=status.HTTP_204_NO_CONTENT)
    
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return custom_response(
            True,
            "Comments fetched successfully",
            serializer.data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return custom_response(
                True,
                "Comment created successfully",
                serializer.data,
                status_code=status.HTTP_201_CREATED
            )

        return custom_response(
            False,
            "Validation failed",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())

        return custom_response(
            True,
            "Comment fetched successfully",
            serializer.data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object(),
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return custom_response(
                True,
                "Comment updated successfully",
                serializer.data,
                status_code=status.HTTP_200_OK
            )

        return custom_response(
            False,
            "Validation failed",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()

        return custom_response(
            True,
            "Comment deleted successfully",
            status_code=status.HTTP_204_NO_CONTENT
        )

class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
