from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='articles'),
    path('article/<int:article_id>', views.article_detail, name='article'),
    path('article/create', views.article_create, name='create_article'),
    path('article/delete/<int:article_id>', views.delete_user_article, name='delete_article'),
    path('user/<int:user_id>', views.user_profile, name='user_profile'),
    path('user/<int:user_id>/articles', views.update_user_articles, name='user_articles'),
]
