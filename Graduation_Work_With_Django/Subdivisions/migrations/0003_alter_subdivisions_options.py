# Generated by Django 4.2.5 on 2024-04-20 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Subdivisions', '0002_alter_subdivisions_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subdivisions',
            options={'permissions': [('subdivision_add', 'Добавление подразделения'), ('subdivision_change', 'Изменение подразделения'), ('subdivision_delete', 'Удаление подразделения'), ('subdivision_id', 'Просмотр подразделения'), ('subdivision_map', 'Просмотр всех подразделений на карте'), ('subdivision_all', 'Просмотр всех подразделений в таблице')], 'verbose_name': 'Подразделение', 'verbose_name_plural': 'Подразделения'},
        ),
    ]
