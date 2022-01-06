# Generated by Django 3.2.9 on 2022-01-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_language_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.CharField(max_length=60, null=True, verbose_name='پیوند یکتا'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='language_field',
            field=models.CharField(blank=True, choices=[('persian', 'persian'), ('english', 'english')], max_length=256, null=True, verbose_name='زبان این محتوا'),
        ),
    ]
