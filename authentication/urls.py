from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'auth'


urlpatterns = [
    path('login_user/',login_user_view, name = 'user_login'),
    path('login_service_provider/',login_service_provider_view, name = 'service_provider_login'),
    path('register_user/',register_user_view, name = 'user_reg'),
    path('register_service_provider/',register_Service_Provider_view, name = 'service_provider_reg'),
    
]
