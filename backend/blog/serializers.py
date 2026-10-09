from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.utils.text import slugify
from .models import Category, BlogPost, Comment, Feedback

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    slug = serializers.SlugField(required=False)
    tagline = serializers.CharField(required=False, allow_blank=True, max_length=200)
    display_order = serializers.IntegerField(required=False)
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, obj):
        return obj.posts.filter(status='published').count()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class BlogPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=275)
    slug = serializers.SlugField()
    content = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    status = serializers.ChoiceField(choices=BlogPost.STATUS_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if len(data['password']) < 8:
            raise serializers.ValidationError(
                "Password must contain atleast 8 characters"
            )
        return data



def display_name(user):
    return user.get_full_name() or user.username


class CategoryBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class PostListSerializer(serializers.ModelSerializer):
    category = CategoryBriefSerializer(read_only=True)
    author = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'excerpt', 'hero_image', 'hero_image_alt',
                  'reading_time', 'published_at', 'is_featured', 'category', 'author',
                  'like_count', 'comment_count']

    def get_author(self, obj):
        return display_name(obj.author)

    def get_like_count(self, obj):
        return getattr(obj, 'like_count', None) if hasattr(obj, 'like_count') else obj.likes.count()

    def get_comment_count(self, obj):
        return obj.comment_count if hasattr(obj, 'comment_count') else obj.comments.count()


class PostDetailSerializer(PostListSerializer):
    liked = serializers.SerializerMethodField()

    class Meta(PostListSerializer.Meta):
        fields = PostListSerializer.Meta.fields + ['content', 'status', 'updated_at', 'liked']

    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False


class PostWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    slug = serializers.SlugField(required=False)

    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'category', 'status', 'excerpt',
                  'hero_image', 'hero_image_alt', 'reading_time', 'is_featured']

    def validate(self, attrs):
        if not self.instance and not attrs.get('slug'):
            attrs['slug'] = slugify(attrs['title'])[:50]
        slug = attrs.get('slug')
        if slug:
            clash = BlogPost.objects.filter(slug=slug)
            if self.instance:
                clash = clash.exclude(pk=self.instance.pk)
            if clash.exists():
                raise serializers.ValidationError({'slug': 'A story with this slug already exists.'})
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    content = serializers.CharField(min_length=2, max_length=1000)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at', 'can_delete']
        read_only_fields = ['id', 'created_at']

    def get_author(self, obj):
        return display_name(obj.user)

    def get_can_delete(self, obj):
        request = self.context.get('request')
        u = getattr(request, 'user', None)
        return bool(u and u.is_authenticated and (u.is_staff or u == obj.user))


TOPIC_CHOICES = ['Therapy', 'Nutrition', 'Movement', 'Mindfulness',
                 'Wellness consultation', 'Not sure yet']


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    topic = serializers.ChoiceField(choices=TOPIC_CHOICES)
    message = serializers.CharField(min_length=10, max_length=3000)

    def create(self, validated_data):
        topic = validated_data['topic']
        return Feedback.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            message=f"Exploring: {topic}\n\n{validated_data['message']}",
        )


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('That username is taken.')
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
