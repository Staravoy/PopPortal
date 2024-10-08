# Generated by Django 5.0.1 on 2024-02-22 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='radio_on_tz',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='car',
            name='use_tz',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='numer_tz',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_tz',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2100)]),
        ),
    ]
