from django.contrib import admin
from .models import ReadNum,ReadDetail

@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('reader_num','content_object')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date','reader_num','content_object')