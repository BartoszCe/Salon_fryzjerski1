from django.urls import path
from .views import SalonDetailView, SalonListView, CustomLoginView, ChangePasswordView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='core:login'), name="logout"),
    path('password/', ChangePasswordView.as_view(), name='password'),
    path('salon/detail/<pk>', SalonDetailView.as_view(), name="salon_detail"),
    path('salon/list/', SalonListView.as_view(), name="salon_list"),
]
