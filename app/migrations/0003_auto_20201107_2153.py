# Generated by Django 3.1.3 on 2020-11-08 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201106_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutpass', models.CharField(default='', max_length=200)),
                ('nombres', models.CharField(default='', max_length=200)),
                ('apellidom', models.CharField(default='', max_length=200)),
                ('apellidop', models.CharField(default='', max_length=200)),
                ('edad', models.IntegerField()),
                ('fechanac', models.DateField(default='')),
                ('paisorig', models.CharField(default='', max_length=200)),
                ('direccion', models.CharField(default='', max_length=200)),
                ('correo', models.EmailField(default='', max_length=200)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]