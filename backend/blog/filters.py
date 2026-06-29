import django_filters

from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )

    class Meta:
        model = BlogPost

        fields = [
            'category',
            'status',
            'title'
        ]