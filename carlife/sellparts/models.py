from django.db import models

# Create your models here.
class Part(models.Model):

    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    name = models.CharField(max_length=40, verbose_name='Название')
    cost = models.FloatField(verbose_name='Цена')
    pic = models.ImageField(max_length=100, verbose_name='Картинка')
