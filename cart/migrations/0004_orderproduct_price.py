# Generated by Django 4.0.1 on 2022-01-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_orderproduct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
    ]