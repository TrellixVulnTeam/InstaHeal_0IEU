# Generated by Django 2.0.2 on 2020-09-13 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_date_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
