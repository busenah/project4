from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='patients')
    title = models.CharField(max_length=100, default="patient's name")
    # name = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="patient's phone number")
    address = models.CharField(
        max_length=100, default="patient's physical address")
    next_of_kin = models.CharField(
        max_length=100, default="patient's next of kin")

    time = models.CharField(max_length=100, default='no preferred time')
    date = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title
