# Generated by Django 3.0.5 on 2021-06-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0042_auto_20210608_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='inquiry_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]