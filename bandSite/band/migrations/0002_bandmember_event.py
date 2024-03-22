# Generated by Django 5.0.2 on 2024-02-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]