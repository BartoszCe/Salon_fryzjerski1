# Generated by Django 3.2.7 on 2021-10-30 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('employee', models.CharField(blank=True, max_length=50, null=True, verbose_name='Employee')),
                ('color', models.CharField(choices=[('#eeeeee', 'gray'), ('#ff0000', 'red'), ('#0000ff', 'blue'), ('#00ff00', 'green'), ('#000000', 'black'), ('#ffffff', 'white'), ('#7E8F7C', 'khaki')], default='gray', max_length=7, verbose_name='Color')),
                ('private', models.BooleanField(default=False, verbose_name='Private')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('related_activity', models.ManyToManyField(blank=True, to='Calendary.Activity', verbose_name='Related Activities')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
    ]