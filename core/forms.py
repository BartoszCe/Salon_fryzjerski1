from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from core.models import Employee


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ('old_password', 'new_password1', 'new_password2',)
