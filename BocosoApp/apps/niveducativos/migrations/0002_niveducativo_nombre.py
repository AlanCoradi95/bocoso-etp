# Generated by Django 4.2.4 on 2023-09-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niveducativos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='niveducativo',
            name='nombre',
            field=models.CharField(default='Sin especificar', max_length=40),
        ),
    ]
