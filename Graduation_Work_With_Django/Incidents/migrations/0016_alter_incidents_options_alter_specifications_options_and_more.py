# Generated by Django 4.2.5 on 2024-04-21 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0015_alter_incidents_options_alter_incidents_time_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidents',
            options={'permissions': [('Incidents.incidents_add', 'Добавление происшествий'), ('Incidents.incidents_change', 'Изменение происшествий'), ('Incidents.incidents_delete', 'Удаление происшествий'), ('Incidents.incidents_id', 'Просмотр происшествия'), ('Incidents.incidents_map', 'Просмотр всех происшествий на карте'), ('Incidents.incidents_all', 'Просмотр всех происшествий в таблице')], 'verbose_name': 'Происшествие', 'verbose_name_plural': 'Происшествия'},
        ),
        migrations.AlterModelOptions(
            name='specifications',
            options={'permissions': [('Incidents.specification_add', 'Добавление спецификации происшествия'), ('Incidents.specification_change', 'Изменение спецификации происшествия'), ('Incidents.specification_delete', 'Удаление спецификации происшествия'), ('Incidents.specification_id', 'Просмотр спецификации происшествия'), ('Incidents.specification_all', 'Просмотр всех спецификаций в таблице')], 'verbose_name': 'Спецификацию происшествия', 'verbose_name_plural': 'Спецификации происшествий'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'permissions': [('Incidents.status_add', 'Добавление статуса происшествия'), ('Incidents.status_change', 'Изменение статуса происшествия'), ('Incidents.status_delete', 'Удаление статуса происшествия'), ('Incidents.status_id', 'Просмотр статуса происшествия'), ('Incidents.status_all', 'Просмотр всех статусов в таблице')], 'verbose_name': 'Статус происшествия', 'verbose_name_plural': 'Статусы происшествий'},
        ),
        migrations.AlterField(
            model_name='incidents',
            name='time_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 21, 14, 53, 54, 756347), verbose_name='Дата и время обнаружения происшествия'),
        ),
    ]
