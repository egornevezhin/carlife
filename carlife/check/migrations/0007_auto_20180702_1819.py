# Generated by Django 2.0.3 on 2018-07-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_auto_20180702_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='problem',
            field=models.TextField(null=True, verbose_name='Проблема'),
        ),
        migrations.AlterField(
            model_name='order',
            name='car_number',
            field=models.CharField(max_length=12, null=True, verbose_name='Номер машины'),
        ),
    ]