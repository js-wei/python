# @Author: 魏巍
# @Date:   2017-11-02T10:48:18+08:00
# @Email:  524314430@qq.com
# @Last modified by:   魏巍
# @Last modified time: 2017-11-02T18:21:10+08:00



from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'hits', 'status', 'pub_date', 'update_time')
    search_fields = ['title']
    list_filter = ('status',)

admin.site.register(Article,ArticleAdmin)
