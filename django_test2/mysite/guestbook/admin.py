from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'creation_date')
    list_filter = ('author', 'creation_date')
    search_fields = ('author', 'message')
