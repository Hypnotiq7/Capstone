# Generated by Django 5.0.2 on 2024-02-17 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0002_bandmember_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BandMember',
        ),
    ]