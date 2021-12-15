# Generated by Django 3.2.9 on 2021-12-15 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_auto_20211215_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puntodeventa',
            old_name='sucursal',
            new_name='barrio',
        ),
        migrations.RemoveField(
            model_name='puntodeventa',
            name='calle',
        ),
        migrations.AddField(
            model_name='puntodeventa',
            name='mail',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='puntodeventa',
            name='nombre',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
