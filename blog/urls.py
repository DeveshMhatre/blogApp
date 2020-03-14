from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='articles'),
    path('article/<int:article_id>', views.article_detail, name='article'),
]
