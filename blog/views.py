from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Article

@login_required(login_url='accounts:login')
def article_list(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_article_list': latest_article_list
    }
    return render(request, 'blog/article_list.html', context)

@login_required(login_url='accounts:login')
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'blog/article_detail.html', context)
