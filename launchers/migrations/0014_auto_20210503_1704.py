# Generated by Django 3.2 on 2021-05-03 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0013_break_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='break_time',
            new_name='break_times',
        ),
        migrations.RenameField(
            model_name='break_times',
            old_name='login_user',
            new_name='name',
        ),
    ]
