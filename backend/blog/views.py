from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .pagination import BlogPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.throttling import ScopedRateThrottle
from django.db.models import Count, Q

from .models import Category, BlogPost, Comment, Like
from .pagination import PostPagination
from .permissions import IsOwnerOrStaffOrReadOnly
from .serializers import (CategorySerializer, BlogPostSerializer, PostListSerializer,
                          PostDetailSerializer, PostWriteSerializer, CommentSerializer,
                          ContactSerializer, RegisterSerializer, display_name)

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



# ---------------------------------------------------------------------------
# Editorial API (additive): used by THE WITHIN front end
# ---------------------------------------------------------------------------

def annotated_posts():
    return (BlogPost.objects.select_related('category', 'author')
            .annotate(like_count=Count('likes', distinct=True),
                      comment_count=Count('comments', distinct=True))
            .order_by('-published_at', '-created_at'))


class PostListCreateView(ListCreateAPIView):
    """GET /api/posts/?category=&q=&featured=&page=   POST (auth) creates a story."""
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return PostWriteSerializer if self.request.method == 'POST' else PostListSerializer

    def get_queryset(self):
        qs = annotated_posts().filter(status='published')
        p = self.request.query_params
        cat = p.get('category')
        if cat:
            qs = qs.filter(Q(category__slug__iexact=cat) | Q(category__name__iexact=cat))
        q = (p.get('q') or p.get('search') or '').strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(excerpt__icontains=q) |
                           Q(content__icontains=q) | Q(category__name__icontains=q))
        if p.get('featured') in ('1', 'true'):
            qs = qs.filter(is_featured=True)
        return qs

    def create(self, request, *args, **kwargs):
        ser = PostWriteSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        post = ser.save(author=request.user)
        return Response(PostDetailSerializer(post, context={'request': request}).data,
                        status=status.HTTP_201_CREATED)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE /api/posts/<slug>/"""
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrStaffOrReadOnly]

    def get_queryset(self):
        qs = annotated_posts()
        u = self.request.user
        if u.is_authenticated and u.is_staff:
            return qs
        if u.is_authenticated:
            return qs.filter(Q(status='published') | Q(author=u))
        return qs.filter(status='published')

    def get_serializer_class(self):
        return PostWriteSerializer if self.request.method in ('PUT', 'PATCH') else PostDetailSerializer

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        ser = PostWriteSerializer(post, data=request.data, partial=kwargs.get('partial', False))
        ser.is_valid(raise_exception=True)
        post = ser.save()
        return Response(PostDetailSerializer(post, context={'request': request}).data)


class RelatedPostsView(APIView):
    def get(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug, status='published')
        same = list(annotated_posts().filter(status='published', category=post.category).exclude(pk=post.pk)[:3])
        if len(same) < 3:
            ids = [post.pk] + [p.pk for p in same]
            same += list(annotated_posts().filter(status='published').exclude(pk__in=ids)[:3 - len(same)])
        return Response(PostListSerializer(same, many=True).data)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def _post(self, slug):
        return get_object_or_404(BlogPost, slug=slug, status='published')

    def post(self, request, slug):
        post = self._post(slug)
        _, created = Like.objects.get_or_create(post=post, user=request.user)
        return Response({'liked': True, 'like_count': post.likes.count()},
                        status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    def delete(self, request, slug):
        post = self._post(slug)
        Like.objects.filter(post=post, user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug, status='published')
        qs = post.comments.select_related('user').order_by('-created_at')
        return Response(CommentSerializer(qs, many=True, context={'request': request}).data)

    def post(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug, status='published')
        ser = CommentSerializer(data=request.data, context={'request': request})
        ser.is_valid(raise_exception=True)
        ser.save(post=post, user=request.user)
        return Response(ser.data, status=status.HTTP_201_CREATED)


class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if not (request.user.is_staff or comment.user == request.user):
            return Response({'detail': 'You can only remove your own comments.'},
                            status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'contact'

    def post(self, request):
        ser = ContactSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response({'detail': 'Thank you. Your enquiry has been received.'},
                        status=status.HTTP_201_CREATED)


class RegisterView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'register'

    def post(self, request):
        ser = RegisterSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        u = request.user
        return Response({'id': u.id, 'username': u.username, 'name': display_name(u), 'is_staff': u.is_staff})
