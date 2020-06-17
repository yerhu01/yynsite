from django.contrib import admin

from .models import Category, Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
