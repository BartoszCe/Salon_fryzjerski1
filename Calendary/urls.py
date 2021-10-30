from django.urls import path
from . import views

app_name = 'calendary'

urlpatterns = [
    path('', views.calendar, name='main_calendar'),
    path('<user>', views.view_page, name='view_page'),
    path('get/<id>', views.get_data, name='get_data'),
    path('delete/<id>', views.delete_data, name='delete_data'),
    path('save/<id>', views.save_data, name='save_data'),
]