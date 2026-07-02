from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .pagination import BlogPagination
from rest_framework.permissions import IsAuthenticated

from .models import Category, BlogPost
from .serializers import CategorySerializer, BlogPostSerializer

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryAPIView(APIView):
    def get(self, request):
        name = request.GET.get('name')

        if name:
            try:
                category = Category.objects.get(name=name)
                posts = BlogPost.objects.filter(category=category)
                serializer = BlogPostSerializer(posts, many=True)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
            
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class AllBlogPostsAPIView(APIView):
    def get(self, request):
        try:
            posts = BlogPost.objects.all()
            paginator = BlogPagination()
            paginated_posts = paginator.paginate_queryset(posts, request)
            serializer = BlogPostSerializer(paginated_posts, many=True)

            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class BlogPostAPIView(APIView):
    def get(self, request):
        title = request.GET.get('title')
        if title:
            try:
                post = BlogPost.objects.get(title=title)
                serializer = BlogPostSerializer(post)
                return Response(serializer.data)
            except BlogPost.DoesNotExist:
                return Response({"error": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)
            
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)
    
class BlogPostCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)