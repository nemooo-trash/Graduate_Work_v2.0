# Generated by Django 4.2.5 on 2024-04-20 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_positions_options_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('user_id', 'Просмотр пользователей'), ('user_delete', 'Удаление пользователей'), ('user_all', 'Просмотр всех пользователей в таблице')], 'verbose_name': 'Пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
