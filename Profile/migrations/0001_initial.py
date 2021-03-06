# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-21 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('body', models.TextField(max_length=5000)),
                ('Email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Myobjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoftwareEngineering', models.CharField(max_length=1000)),
                ('ComputerEngineering', models.CharField(max_length=1000)),
                ('skills', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='myprojects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='')),
                ('matlab_file', models.FileField(upload_to='')),
                ('excel_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('DateofBirth', models.CharField(max_length=250)),
                ('PermanentAddress', models.CharField(max_length=250)),
                ('PresentAddress', models.CharField(max_length=250)),
                ('Education', models.CharField(max_length=250)),
                ('University', models.CharField(max_length=250)),
                ('GraduationDate', models.CharField(max_length=250)),
                ('Contact', models.CharField(max_length=250)),
                ('EmailAddress', models.EmailField(max_length=100)),
                ('LinkedIn_id', models.CharField(max_length=250)),
                ('Facebook_id', models.CharField(max_length=250)),
                ('github_id', models.CharField(max_length=250)),
            ],
        ),
    ]
