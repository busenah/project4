from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=100, default="Patient's name")
    phone_number = models.CharField(max_length=100, default="patient's phone number")
    address = models.CharField(max_length=100, default="Patient's physical address")
    symptoms = models.CharField(max_length=100, default='Description or Symtpoms')
    time = models.CharField(max_length=100, default='no preferred time')
    date = models.CharField(max_length=100, default='no preferred date')
    doctor_to_see = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
