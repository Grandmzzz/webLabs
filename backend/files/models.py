from django.db import models


class File(models.Model):
    path = models.CharField('Путь до файла', max_length=256, default='')
