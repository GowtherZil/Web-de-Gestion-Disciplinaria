# Generated by Django 3.2.9 on 2022-01-06 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0030_auto_20220106_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='p_guia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comision_p_guia', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comision',
            name='presidente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comision_presidente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comision',
            name='secretario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comision_secretario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comision',
            name='v_feu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comision_v_feu', to=settings.AUTH_USER_MODEL),
        ),
    ]