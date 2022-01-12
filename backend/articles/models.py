from django.contrib.auth.models import User
from django.db import models

from files.models import File


class Tag(models.Model):
    description = models.CharField('Описание тега', max_length=256, default='')


class Article(models.Model):
    title = models.CharField('Заголовок статьи', max_length=512, default='')
    text = models.TextField('Текст статьи')
    image = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)
    date_create = models.DateTimeField('Дата публикации', auto_now_add=True)
    description = models.CharField('Краткое описание для отображения в ленте', max_length=512, default='')
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
