# Generated by Django 4.0.3 on 2022-03-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_grupos_alter_usuarios_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='criado',
            field=models.DateField(),
        ),
    ]
