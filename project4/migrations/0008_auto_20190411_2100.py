# Generated by Django 2.2 on 2019-04-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4', '0007_patient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default="patient's physical address", max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='next_of_kin',
            field=models.CharField(default="patient's next of kin", max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default="patient's phone number", max_length=100),
        ),
    ]
