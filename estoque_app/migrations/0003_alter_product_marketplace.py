# Generated by Django 4.2.11 on 2024-12-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque_app', '0002_product_marketplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='marketplace',
            field=models.JSONField(default=dict),
        ),
    ]
