# Generated by Django 3.2.5 on 2023-08-11 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquorList', '0005_alter_liquor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquor',
            name='numberOfBottles',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]