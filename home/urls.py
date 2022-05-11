from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'main'


urlpatterns = [
    path('',index, name = "home"),
    path('user_dashboard/',user_dashboard_view, name = "user_dashboard"),
    path('service_provider_dashboard/',service_provider_dashboard_view, name = "service_provider_dashboard"),
    path('all_services/',all_services, name = "all_services"),
    path('service_provider/',service_provider_dashboard, name = "service_provider"),
    path('user_requests/',user_requests, name = "user_requests"),
    path('service_provider_profile/',service_provider_profile, name = "service_provider_profile"),

    path('edit_service/',update_service_view, name = "update_service"),
    path('service_deleted/<int:id>/',delete_service_view, name = "delete_service")
    
]
