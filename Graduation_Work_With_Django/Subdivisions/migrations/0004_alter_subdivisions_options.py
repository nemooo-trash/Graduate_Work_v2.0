# Generated by Django 4.2.5 on 2024-04-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subdivisions', '0003_alter_subdivisions_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subdivisions',
            options={'permissions': [('Subdivisions.subdivision_add', 'Добавление подразделения'), ('Subdivisions.subdivision_change', 'Изменение подразделения'), ('Subdivisions.subdivision_delete', 'Удаление подразделения'), ('Subdivisions.subdivision_id', 'Просмотр подразделения'), ('Subdivisions.subdivision_map', 'Просмотр всех подразделений на карте'), ('Subdivisions.subdivision_all', 'Просмотр всех подразделений в таблице')], 'verbose_name': 'Подразделение', 'verbose_name_plural': 'Подразделения'},
        ),
    ]
