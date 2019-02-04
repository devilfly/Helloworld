from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('content_object','text','comment_time','user','root','parent')