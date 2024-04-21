# Generated by Django 4.2.5 on 2024-04-20 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positions',
            options={'permissions': [('position_add', 'Добавление должностей'), ('position_change', 'Изменение должностей'), ('position_delete', 'Удаление должностей'), ('position_id', 'Просмотр должности'), ('position_all', 'Просмотр всех должностей в таблице')], 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('user_id', 'Просмотр пользователей'), ('user_all', 'Просмотр всех пользователей в таблице')], 'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
