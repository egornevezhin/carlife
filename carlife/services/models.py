from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Master(models.Model):

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    name = models.CharField(max_length=30, verbose_name='ФИО')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Телефон')
    work = models.CharField(max_length=20, verbose_name='Область работы')

    def __str__(self):
        return self.name


class Service(models.Model):

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    name = models.CharField(max_length=40, verbose_name='Название')
    cost_1 = models.CharField(max_length=10, verbose_name='Легковые (A, B, C)', null=True)
    cost_2 = models.CharField(max_length=10, verbose_name='Легковые (D, E, F)', null=True)
    cost_3 = models.CharField(max_length=10, verbose_name='Джипы и минивены', null=True)
    person = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return self.name
