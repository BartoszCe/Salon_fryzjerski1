# Generated by Django 3.2.6 on 2021-10-22 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_employe_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='surname',
        ),
    ]
