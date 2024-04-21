# Generated by Django 4.2.5 on 2024-04-20 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.ForeignKey(blank=True, default=10, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.positions', verbose_name='Должность'),
        ),
    ]
