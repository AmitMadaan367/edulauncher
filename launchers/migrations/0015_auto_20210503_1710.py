# Generated by Django 3.2 on 2021-05-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0014_auto_20210503_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filenote',
            name='note',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='last_follow_up_text',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
