# Generated by Django 2.0.3 on 2018-07-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Номер заказа'),
        ),
    ]
