from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Additive fields (migration 0004) used by the editorial front end.
    slug = models.SlugField(max_length=100, blank=True, default='')
    tagline = models.CharField(max_length=200, blank=True, default='')
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]

    title = models.CharField(max_length=275)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Additive editorial fields (migration 0004).
    excerpt = models.TextField(blank=True, default='')
    hero_image = models.CharField(max_length=300, blank=True, default='')
    hero_image_alt = models.CharField(max_length=300, blank=True, default='')
    reading_time = models.PositiveSmallIntegerField(default=0)
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        if not self.reading_time and self.content:
            self.reading_time = max(1, round(len(self.content.split()) / 200))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# --- Models created by existing migration 0003, restored here so the model
# --- state matches migration history (no data is changed by this).

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user} likes {self.post}"
