# Generated by Django 4.0.5 on 2022-06-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rh', '0006_alter_funcionario_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
    ]