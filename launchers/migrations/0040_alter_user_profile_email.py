# Generated by Django 3.2 on 2021-05-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0039_alter_user_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='Email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
