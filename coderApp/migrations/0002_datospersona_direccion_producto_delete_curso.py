# Generated by Django 4.0 on 2022-01-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='datosPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50, verbose_name='calle')),
                ('altura', models.CharField(max_length=50, verbose_name='altura')),
                ('localidad', models.CharField(max_length=50, verbose_name='localidad')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50, verbose_name='producto')),
                ('tipo', models.CharField(max_length=50, verbose_name='tipo')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
