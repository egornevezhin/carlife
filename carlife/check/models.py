from django.db import models
from django.utils import timezone

# Create your models here.


class Order(models.Model):

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    name = models.CharField(max_length=40, verbose_name='ФИО заказчика')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    car_number = models.CharField(max_length=12, verbose_name='Номер машины')
    date = models.DateField(verbose_name='Дата заказа', default=timezone.now)
    status = models.ForeignKey('Status', verbose_name='Статус', default=1, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Status(models.Model):

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    status = models.CharField(max_length=40, verbose_name='Статус')

    def __str__(self):
        return self.status

