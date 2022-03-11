from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'main'


urlpatterns = [
    path('',index, name = "home"),
    path('user_dashboard/',user_dashboard_view, name = "user_dashboard"),
    path('service_provider_dashboard/',service_provider_dashboard_view, name = "service_provider_dashboard"),
    
]
