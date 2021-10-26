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


class Visit(models.Model):
    salon = models.ForeignKey(Salon, related_name='visit', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, related_name='visit', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, blank=True)
    start_time = models.TimeField(verbose_name="Start Time")
    date = models.DateField(verbose_name="Date")
    comment = models.TextField(verbose_name="Comment", blank=True, null=True)
    related_activity = models.ManyToManyField('Activity', verbose_name="Related Activities", blank=True)

    def __str__(self):
        return self.name + " " + str(self.start_time) + " " + str(self.date)

    def save(self, *args, **kwargs):
        if(self.id != None):
            for i in self.related_activity.all():
                i.delete()
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        return super().delete()

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"