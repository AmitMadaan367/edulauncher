# Generated by Django 3.0.5 on 2021-04-30 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0006_auto_20210430_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='hotel_Main_Img',
            new_name='profile_pic',
        ),
    ]
