from django.db import models


# для class Post в models.py создаем фильтр по умолчанию по "published"
class PostPublishedManager(models.Manager):
    def get_queryset(self):
        return (super(PostPublishedManager, self)
                .get_queryset()
                .filter(status='published'))
