from django.shortcuts import render, HttpResponse



# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def user_dashboard_view(request):
    return render(request, 'user/user_page.html')

def service_provider_dashboard_view(request):
    return render(request, 'service_provider/service_provider_page.html')

def all_services(request):
    return render(request, 'service_provider/view_services.html')

def service_provider_dashboard(request):
    return render(request, 'service_provider/service_provider_dashboard.html')

def user_requests(request):
    return render(request, 'service_provider/user_requests.html')

def service_provider_profile(request):
    return render(request, 'service_provider/service_provider_profile.html')




