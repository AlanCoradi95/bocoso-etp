# Generated by Django 4.2.4 on 2023-09-09 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
    ]
