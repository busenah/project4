# Generated by Django 2.2 on 2019-04-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4', '0006_auto_20190411_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default="patient's full name", max_length=100),
        ),
    ]