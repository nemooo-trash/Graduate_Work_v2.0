# Generated by Django 4.2.5 on 2023-10-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='e-mail'),
        ),
    ]