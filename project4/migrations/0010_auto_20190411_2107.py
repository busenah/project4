# Generated by Django 2.2 on 2019-04-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4', '0009_auto_20190411_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='title',
            field=models.CharField(default="patient's title", max_length=100),
        ),
    ]