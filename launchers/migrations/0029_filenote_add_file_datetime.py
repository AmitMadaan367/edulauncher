# Generated by Django 3.2 on 2021-05-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0028_remove_filenote_ssd'),
    ]

    operations = [
        migrations.AddField(
            model_name='filenote',
            name='add_file_datetime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]