from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'auth'


urlpatterns = [
    path('user_authentication/',login_user_view, name = 'user_authentication'),
    path('user_registration/',register_user_view, name = 'user_registration'),
    
        
]
