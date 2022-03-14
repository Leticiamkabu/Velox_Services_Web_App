from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'dashboard'


urlpatterns = [
    path('admin_dashboard/',admin_dashboard_view, name = "admin_dashboard"),
    path('base/',testing, name = "t")

    
    
]