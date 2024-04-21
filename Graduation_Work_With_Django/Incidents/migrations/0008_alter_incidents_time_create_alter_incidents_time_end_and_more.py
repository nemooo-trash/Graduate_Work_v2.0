# Generated by Django 4.2.5 on 2024-04-20 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0007_alter_incidents_options_alter_specifications_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='time_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 20, 17, 40, 49, 278618), verbose_name='Дата и время обнаружения происшествия'),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время ликвидирования происшествия'),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время принятия решения'),
        ),
    ]
