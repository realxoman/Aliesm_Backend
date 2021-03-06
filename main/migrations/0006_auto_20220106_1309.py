# Generated by Django 3.2.9 on 2022-01-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220106_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='language_field',
            field=models.CharField(blank=True, choices=[('persian', 'persian'), ('english', 'english')], max_length=256, null=True, verbose_name='زبان این محتوا'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین بروزرسانی'),
        ),
        migrations.AddField(
            model_name='educations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='educations',
            name='language_field',
            field=models.CharField(blank=True, choices=[('persian', 'persian'), ('english', 'english')], max_length=256, null=True, verbose_name='زبان این محتوا'),
        ),
        migrations.AddField(
            model_name='educations',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین بروزرسانی'),
        ),
        migrations.AddField(
            model_name='experiences',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='experiences',
            name='language_field',
            field=models.CharField(blank=True, choices=[('persian', 'persian'), ('english', 'english')], max_length=256, null=True, verbose_name='زبان این محتوا'),
        ),
        migrations.AddField(
            model_name='experiences',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین بروزرسانی'),
        ),
        migrations.AddField(
            model_name='settings',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='settings',
            name='language_field',
            field=models.CharField(blank=True, choices=[('persian', 'persian'), ('english', 'english')], max_length=256, null=True, verbose_name='زبان این محتوا'),
        ),
        migrations.AddField(
            model_name='settings',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین بروزرسانی'),
        ),
        migrations.AddField(
            model_name='skills',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AddField(
            model_name='skills',
            name='language_field',
            field=models.CharField(blank=True, choices=[('persian', 'persian'), ('english', 'english')], max_length=256, null=True, verbose_name='زبان این محتوا'),
        ),
        migrations.AddField(
            model_name='skills',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='آخرین بروزرسانی'),
        ),
    ]
