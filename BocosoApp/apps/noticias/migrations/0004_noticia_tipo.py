# Generated by Django 4.2.4 on 2023-09-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_alter_noticia_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='tipo',
            field=models.IntegerField(default=1),
        ),
    ]