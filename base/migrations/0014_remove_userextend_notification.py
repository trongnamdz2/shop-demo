# Generated by Django 4.2 on 2023-05-04 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_userextend_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextend',
            name='notification',
        ),
    ]
