# Generated by Django 3.2 on 2021-05-10 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('launchers', '0035_alter_loginhistory_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]