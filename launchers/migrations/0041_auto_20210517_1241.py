# Generated by Django 3.2 on 2021-05-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0040_alter_user_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginhistory',
            name='start_break',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='loginhistory',
            name='stop_break',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]