# Generated by Django 3.2 on 2021-05-05 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0027_filenote_ssd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filenote',
            name='ssd',
        ),
    ]
