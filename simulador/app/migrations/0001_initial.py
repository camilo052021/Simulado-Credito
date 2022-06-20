# Generated by Django 4.0.5 on 2022-06-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PruebaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_pruebas', models.CharField(max_length=30, verbose_name='Usuario Pruebas')),
                ('nombre_pruebas', models.CharField(max_length=30, verbose_name='Usuario Pruebas')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='Creado el')),
                ('modify_at', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Usuario Prueba',
                'verbose_name_plural': 'Usuarios Pruebas',
            },
        ),
    ]
