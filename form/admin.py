from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    list_filter = ['first_name', 'age']
    search_fields = ['first_name', 'last_name', 'username']
    ordering = ['first_name', 'last_name']
