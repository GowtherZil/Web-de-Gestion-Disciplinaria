# Generated by Django 3.2.9 on 2022-01-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_perfil_un_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cargo',
            field=models.CharField(choices=[('-----', '-----'), ('Profesor', 'Profesor'), ('J. Apto', 'J. Apto'), ('J. Asig', 'J. Asig')], default='1', max_length=8),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cat_d',
            field=models.CharField(choices=[('-----', '-----'), ('Titular', 'Titular'), ('Adiestrado', 'Adiestrado'), ('Instructor', 'Instructor')], default='1', max_length=10),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rol',
            field=models.CharField(choices=[('Usuario', 'Usuario'), ('Admin', 'Admin')], default='1', max_length=7),
        ),
    ]
