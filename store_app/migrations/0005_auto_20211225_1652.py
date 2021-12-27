# Generated by Django 3.2.7 on 2021-12-25 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]