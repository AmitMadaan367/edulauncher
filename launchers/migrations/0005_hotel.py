# Generated by Django 3.0.5 on 2021-04-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchers', '0004_auto_20210429_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
