from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'main'


urlpatterns = [
    path('',index, name = "home"),
    path('user_page/',user_page_view, name = "user_page"),
    path('user_dashboard/',user_dashboard_view, name = "user_dashboard"),
    path('service_requested_dashboard/',service_requested_view, name = "service_requested"),
    path('user_profile/',user_profile_view, name = "user_profile"),
    path('user_request_deleted/<int:id>/',delete_user_request_view, name = "delete_user_request"),
    path('service detail/<int:id>/',view_service_details_view, name = "view_service_details"),
    
    # service provider section
    path('service_provider_dashboard/',service_provider_dashboard_view, name = "service_provider_dashboard"),
    path('all_services/',all_services, name = "all_services"),
    # path('service_provider_dashboard/',service_provider_dashboard, name = "service_provider"),
    path('user_requests/',user_requests, name = "user_requests"),
    path('service_provider_profile/',service_provider_profile, name = "service_provider_profile"),

    path('<int:id>/',update_service_view, name = "update_service"),
    path('service_deleted/<int:id>/',delete_service_view, name = "delete_service"),
    # path('create_service_form/',form_view, name = "form_display"),
    
    path('logout/',user_logout, name = "logout")
    
]
