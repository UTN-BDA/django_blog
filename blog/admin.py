from django.contrib import admin
from .models import Author, Post, Page

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')
    search_fields = ('user__username', 'user__email', 'bio')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    list_filter = ('status', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('status', '-published_date')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'order', 'created_date')
    list_filter = ('is_published', 'created_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order',)
