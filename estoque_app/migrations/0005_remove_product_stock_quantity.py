# Generated by Django 4.2.11 on 2024-12-18 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_app', '0004_alter_product_marketplace'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock_quantity',
        ),
    ]
