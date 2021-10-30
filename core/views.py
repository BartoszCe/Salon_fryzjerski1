from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from phonenumbers.unicode_util import Category

from .forms import ChangePasswordForm
from .models import Salon, Employee, Visit
from django.views.generic import DetailView, ListView


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


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('core:salon_list')


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('core:salon_list')



class SalonDetailView(LoginRequiredMixin, DetailView):
    login_url = 'core:login'
    template_name = 'salon_detail.html'
    model = Salon

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.order_by('name')
        return context


class SalonListView(LoginRequiredMixin, ListView):
    login_url = 'core:login'
    template_name = 'salon_list.html'
    model = Salon

