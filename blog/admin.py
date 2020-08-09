from django.contrib import admin
from .models import Post
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_filter = ('title','body')
    prepopulatedFeild = {'slug':('title',)}
    date_h = 'publish'
    ordering = ('status','publish')