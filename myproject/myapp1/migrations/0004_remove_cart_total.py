# Generated by Django 5.1.4 on 2025-01-29 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
