# Generated by Django 4.2.5 on 2024-04-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0003_alter_incidents_description_alter_incidents_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidents',
            name='pattern',
            field=models.CharField(default='123', max_length=20, verbose_name='Характеристика инцидента'),
        ),
    ]
