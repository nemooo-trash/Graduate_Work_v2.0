# Generated by Django 4.2.5 on 2024-04-20 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0011_alter_incidents_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='time_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 20, 20, 27, 49, 828984), verbose_name='Дата и время обнаружения происшествия'),
        ),
    ]