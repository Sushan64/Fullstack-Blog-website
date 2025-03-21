from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    list_filter = ('category', 'published_date')
    search_fields = ['title', 'text']
    prepopulated_fields = {'category': ('title',)}