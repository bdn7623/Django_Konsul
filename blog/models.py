from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .managers import PostPublishedManager


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True) # только допустимые сымволы в адресной строке

    class Meta:
        verbose_name_plural = 'categories' # как будет во множественнои числе
        ordering = ('name',) # 1) сортируем по умолчанию по "name". 2) ставим "," чтобы был кортеж

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), #1e как будет отображаться в базе данных, 2е у пользователя
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts') # это поле позволить связать user.posts
    body = models.TextField(verbose_name='Content')
    publish = models.DateTimeField(default=timezone.localtime)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image_url = models.URLField(max_length=255)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='posts') # это поле позволить связать category.posts
    objects = models.Manager()
    published = PostPublishedManager() #создаем фильтрв по полю 'published' в managers.py

    class Meta:
        ordering = ('-publish', '-created')

    def __str__(self):
        return self.title
