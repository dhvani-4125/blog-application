from django.contrib import admin
from .models import (Category, BlogPost, Comment, Like, Feedback)

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Feedback)
