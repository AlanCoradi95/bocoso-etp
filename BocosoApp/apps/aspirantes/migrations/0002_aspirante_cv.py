# Generated by Django 4.2.4 on 2023-09-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspirantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirante',
            name='cv',
            field=models.FileField(blank=True, upload_to='aspirantes'),
        ),
    ]