from django.contrib import admin
from .models import Salon, Employee


# Register your models here.
@admin.register(Salon)
class Salonadmin(admin.ModelAdmin):
    list_display = ['name', 'adres', 'strona_internetowa']


@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'date_of_birth', 'phone_number', 'email']