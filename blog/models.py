from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    article_title = models.CharField(
        verbose_name='Article title',
        max_length=150,
    )
    article_body = models.TextField(
        verbose_name='Article body',
    )
    pub_date = models.DateTimeField(
        verbose_name='Published on',
        auto_now_add=True,
    )
    mod_date = models.DateTimeField(
        verbose_name='Modified on',
        auto_now=True,
    )

    def __str__(self):
        return self.article_title

    # To check if the article has been modified or not
    def is_moded(self, *args, **kwargs):
        pub = str(self.pub_date).split('.')[0]
        mod = str(self.mod_date).split('.')[0]
        return pub != mod

    class Meta:
        ordering = ['-pub_date']