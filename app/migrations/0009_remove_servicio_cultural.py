# Generated by Django 5.0.3 on 2024-06-26 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_servicio_devocional_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='cultural',
        ),
    ]
