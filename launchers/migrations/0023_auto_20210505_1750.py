# Generated by Django 3.2 on 2021-05-05 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0022_rename_date_filenote_time_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filenote',
            name='time_posted',
        ),
        migrations.AddField(
            model_name='filenote',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
