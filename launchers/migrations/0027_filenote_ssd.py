# Generated by Django 3.2 on 2021-05-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0026_alter_filenote_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='filenote',
            name='ssd',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
