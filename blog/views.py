from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import Article

class ArticleList(ListView):
    model = Article
    context_object_name = 'latest_article_list'
    queryset = Article.objects.order_by('-pub_date')[:5]
    template_name = 'blog/article_list.html'