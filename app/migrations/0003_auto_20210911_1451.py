# Generated by Django 3.1.7 on 2021-09-11 09:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_order_total_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='order',
            new_name='orders',
        ),
    ]
