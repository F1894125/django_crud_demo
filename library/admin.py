from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'summary']
    search_fields = ['title', 'author', 'genre', 'summary']
    list_filter = ['title', 'author', 'genre', 'summary']
    ordering = ['title', 'author', 'genre', 'summary']