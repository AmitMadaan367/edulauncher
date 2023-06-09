# Generated by Django 3.0.5 on 2021-04-29 05:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allcountry', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='idinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, max_length=200, null=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('userid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('advisor', models.CharField(max_length=100)),
                ('reference', models.CharField(blank=True, max_length=200, null=True)),
                ('prefix', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateField(verbose_name=('%d-%m-%Y', '%Y-%m-%d'))),
                ('Email', models.EmailField(max_length=200)),
                ('contact_number', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('correspondence_address', models.CharField(blank=True, max_length=200, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('Gender', models.CharField(blank=True, max_length=200, null=True)),
                ('Marital_Status', models.CharField(blank=True, max_length=200, null=True)),
                ('Country_Preference_a', models.CharField(blank=True, max_length=200, null=True)),
                ('Country_Preference_b', models.CharField(blank=True, max_length=200, null=True)),
                ('Others_Country', models.CharField(blank=True, max_length=200, null=True)),
                ('intake', models.CharField(blank=True, max_length=200, null=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='LeadStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launchers.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Followup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followuphandlername', models.CharField(blank=True, max_length=200, null=True)),
                ('next_followup_notification', models.CharField(blank=True, max_length=200, null=True)),
                ('lastfollowupmtext', models.CharField(blank=True, max_length=1500, null=True)),
                ('lastfollowupdate', models.DateTimeField(default=datetime.datetime.now)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launchers.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='FileNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('note', models.CharField(blank=True, max_length=2000, null=True)),
                ('handler', models.CharField(blank=True, max_length=200, null=True)),
                ('file_note_date', models.CharField(blank=True, max_length=200, null=True)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launchers.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_10', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Class_12', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Passport_Front', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Visa_Stamp', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Graduation_Marksheet', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Resume', models.FileField(blank=True, null=True, upload_to='media/')),
                ('Others', models.FileField(blank=True, null=True, upload_to='media/')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launchers.Profile')),
            ],
        ),
    ]
