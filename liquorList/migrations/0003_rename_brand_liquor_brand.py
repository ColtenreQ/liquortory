# Generated by Django 3.2.5 on 2023-08-08 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liquorList', '0002_liquor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liquor',
            old_name='Brand',
            new_name='brand',
        ),
    ]
