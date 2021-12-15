# Generated by Django 3.2.9 on 2021-12-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntodeventa',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='suscriptor',
            name='telefono',
        ),
        migrations.AlterField(
            model_name='puntodeventa',
            name='calle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='mail',
            field=models.EmailField(max_length=140),
        ),
    ]
