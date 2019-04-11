# Generated by Django 2.2 on 2019-04-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.CharField(default='no preferred date', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='preview_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.CharField(default='no preferred time', max_length=100),
        ),
    ]