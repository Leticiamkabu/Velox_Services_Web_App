from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# from .models import Movie

# Create your views here.

def index(request):
    return render(request, 'home/index.html')
    
# user section
def user_dashboard_view(request):
    return render(request, 'user/user_page.html')

# service provider section
def service_provider_dashboard_view(request):

    form = Create_ServiceForm()
    if request.method == 'POST':
        form = Create_ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            #this saves the form
            form.save()
            # this refreshes the form
            return redirect('/service_provider_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(form.errors)
            for i in form:
                print(i.label)
                print(i.errors)
    

    return render(request, 'service_provider/service_provider_page.html', {'form':form} )


def all_services(request):
    display = Create_Service.objects.all()
    context = {
        'display': display,
    }

    return render(request, 'service_provider/view_services.html', context)

def service_provider_dashboard(request):
    return render(request, 'service_provider/service_provider_dashboard.html')

def user_requests(request):
    return render(request, 'service_provider/user_requests.html')

def service_provider_profile(request):
    return render(request, 'service_provider/service_provider_profile.html')



def update_service_view(request):
    
    return render(request, 'service_provider/service_provider_page.html')

def delete_service_view(request):

    return render(request,'service_provider/view_services.html')


