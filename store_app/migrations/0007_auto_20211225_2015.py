# Generated by Django 3.2.7 on 2021-12-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_alter_order_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.IntegerField(null=True),
        ),
    ]
