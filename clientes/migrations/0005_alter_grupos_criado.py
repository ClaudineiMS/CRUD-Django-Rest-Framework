# Generated by Django 4.0.3 on 2022-03-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_usuarios_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='criado',
            field=models.CharField(max_length=20),
        ),
    ]