# Generated by Django 5.0.1 on 2024-02-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_tz', models.CharField(max_length=50)),
                ('brand_tz', models.CharField(max_length=50)),
                ('model_tz', models.CharField(max_length=50)),
                ('year_tz', models.DateField()),
                ('numer_tz', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=20)),
                ('color_tz', models.CharField(max_length=20)),
                ('balanser_tz', models.CharField(max_length=50)),
                ('condition_tz', models.CharField(max_length=50)),
                ('liable_tz', models.CharField(max_length=200)),
            ],
        ),
    ]
