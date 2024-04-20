# Generated by Django 4.2.5 on 2024-04-19 11:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0003_alter_incidents_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='status',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='Incidents.status', verbose_name='Статус происшествия'),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='time_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 19, 14, 50, 7, 355758), verbose_name='Дата и время обнаружения происшествия'),
        ),
    ]