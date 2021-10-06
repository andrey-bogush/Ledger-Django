# Generated by Django 3.2.7 on 2021-10-06 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0003_auto_20211004_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='inventory_received',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, verbose_name='Total inventory received.'),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='inventory_received_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Total value of inventory received.'),
        ),
    ]
