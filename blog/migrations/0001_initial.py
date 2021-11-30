# Generated by Django 3.2.9 on 2021-11-30 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': '   Posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=256, null=True)),
                ('usermail', models.CharField(blank=True, max_length=256, null=True)),
                ('text', models.TextField()),
                ('date_create', models.DateTimeField()),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': '   Comments',
            },
        ),
    ]
