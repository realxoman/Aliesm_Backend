# Generated by Django 3.2.9 on 2021-11-30 20:37

import ckeditor_uploader.fields
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_name', models.CharField(blank=True, max_length=50, null=True)),
                ('name_of_site', models.CharField(blank=True, default='علی اسمعیلی', max_length=50, null=True)),
                ('slang', models.CharField(blank=True, default='برنامه نویس و تولید کننده محتوا', max_length=50, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=main.models.Homefiles)),
                ('cv', models.FileField(blank=True, null=True, upload_to=main.models.Homefiles)),
                ('info_title1', models.CharField(blank=True, max_length=50, null=True)),
                ('info_content1', models.TextField(blank=True, null=True)),
                ('info_title2', models.CharField(blank=True, max_length=50, null=True)),
                ('info_content2', models.TextField(blank=True, null=True)),
                ('info_title3', models.CharField(blank=True, max_length=50, null=True)),
                ('info_content3', models.TextField(blank=True, null=True)),
                ('info_title4', models.CharField(blank=True, max_length=50, null=True)),
                ('info_content4', models.TextField(blank=True, null=True)),
                ('customers_title', models.CharField(blank=True, max_length=50, null=True)),
                ('customers_num', models.IntegerField(blank=True, null=True)),
                ('years_title', models.CharField(blank=True, max_length=50, null=True)),
                ('years_num', models.IntegerField(blank=True, null=True)),
                ('certificates_title', models.CharField(blank=True, max_length=50, null=True)),
                ('certificates_num', models.IntegerField(blank=True, null=True)),
                ('tea_title', models.CharField(blank=True, max_length=50, null=True)),
                ('tea_num', models.IntegerField(blank=True, null=True)),
                ('videocv', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': ' Settings',
            },
        ),
    ]
