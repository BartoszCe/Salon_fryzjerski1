from django.shortcuts import render, get_object_or_404
from .models import Salon, Employee, Visit


def salon_list(request):
    salon = get_object_or_404(Salon)
    employee = Employee.objects.filter(category=salon)
    return render(request, 'salon.html', {'salon': salon, 'employee': employee})

def employee_detail(request):
    employee = get_object_or_404(Employee)
    return render(request, 'detail.html', {'employee': employee})

def visit_detail(request):
    visit = get_object_or_404(Visit)
    return render(request, 'detail_visit.html', {'visit': visit})
