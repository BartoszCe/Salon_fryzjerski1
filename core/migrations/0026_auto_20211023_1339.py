# Generated by Django 3.2.6 on 2021-10-23 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_salon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='adres',
        ),
        migrations.RemoveField(
            model_name='salon',
            name='strona_internetowa',
        ),
    ]
