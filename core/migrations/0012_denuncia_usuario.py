# Generated by Django 3.2.9 on 2021-12-30 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_denuncia_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='core.usuario'),
            preserve_default=False,
        ),
    ]
