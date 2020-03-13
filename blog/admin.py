from django.contrib import admin

from .models import Article

admin.site.site_header = 'Blog Administration'
admin.site.site_title = 'Blog Administration Area'
admin.site.index_title = 'Welcome to Blog Administration Area'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'user', 'pub_date']
    ordering = ['-pub_date']
    search_fields = ['article_title']

admin.site.register(Article, ArticleAdmin)
