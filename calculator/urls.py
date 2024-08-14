from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gpa_result/', views.gpa_result, name='gpa_result'),
    path('value_error/', views.value_error, name='value_error'),
    path('low_final/', views.low_final, name='low_final'),
    path('low_inyear/', views.low_inyear, name='low_inyear'),
    path('low_year_end/', views.low_year_end, name='low_year_end')
]

