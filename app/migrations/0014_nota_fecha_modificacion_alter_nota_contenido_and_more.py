# Generated by Django 5.0.6 on 2024-07-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='nota',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='nota',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nota',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
