# Generated by Django 4.1.7 on 2023-09-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_position_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(choices=[('Senior Developer', 'Senior Developer'), ('Data Analyst', 'Data Analyst'), ('Manager', 'Manager')], max_length=100),
        ),
    ]
