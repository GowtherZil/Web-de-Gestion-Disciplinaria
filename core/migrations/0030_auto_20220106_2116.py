# Generated by Django 3.2.9 on 2022-01-06 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220106_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expediente',
            name='denuncia',
        ),
        migrations.AddField(
            model_name='denuncia',
            name='comision_a',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.comision'),
        ),
        migrations.AddField(
            model_name='denuncia',
            name='expediente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.expediente'),
        ),
    ]
