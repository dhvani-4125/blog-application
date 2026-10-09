from django.contrib import admin
from .models import Category, BlogPost, Comment, Feedback, Like


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'published_at')
    list_filter = ('status', 'category', 'is_featured')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):  # moderation: staff can review and delete
    list_display = ('post', 'user', 'created_at')
    search_fields = ('content', 'user__username')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Like)
