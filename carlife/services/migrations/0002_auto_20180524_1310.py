# Generated by Django 2.0.3 on 2018-05-24 13:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'Мастер', 'verbose_name_plural': 'Мастера'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=30, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='master',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='master',
            name='work',
            field=models.CharField(max_length=20, verbose_name='Область работы'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cost',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='service',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Master', verbose_name='Работник'),
        ),
    ]