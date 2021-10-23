from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# Create your models here.
class Salon(models.Model):
    name = models.CharField(max_length=40, blank=True)
    adres = models.CharField(max_length=40, blank=True)
    strona_internetowa = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'salons'

    def __str__(self):
        return self.name


class Employee(models.Model):
    salon = models.ForeignKey(Salon, related_name='employee', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(default=timezone.now)
    email = models.EmailField(blank=True)
    phone_number = PhoneNumberField(max_length=12, blank=True)

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name
