from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from authentication.models import *
from .forms import *
from authentication.forms import *
from django.contrib import messages

# from .models import Movie

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

# user section
def user_page_view(request):
    return render(request, 'user/user_main_page.html')

def user_dashboard_view(request):

    service_view = Create_Service.objects.all()
    request_form = Request_ServiceForm()
    if request.method == 'POST':
        request_form = Request_ServiceForm(request.POST, request.FILES)
        if request_form.is_valid():
            #this saves the form
            request_form.save()
            # this refreshes the form
            return redirect('/user_dashboard')

        else:
            print("\n\n\n\n\n\n")
            print(request_form.errors)
            for i in request_form:
                print(i.label)
                print(i.errors)
    
    


    context = {
        'service_view': service_view,
        'request_form': request_form,
    }
    return render(request, 'user/user_dashboard_page.html', context)

def service_requested_view(request):
    requested_services = Request_service.objects.all()


    context = {
        'requested_services': requested_services,
        
    }
    return render(request, 'user/service_requested.html', context)

def view_service_details_view(request, id ):
    display_service = Create_Service.objects.get(id = id)
    print(display_service.id)

    context = {
        'display_service': display_service,
    }
    return render(request, 'user/user_dashboard_page.html', context)

def user_profile_view(request):
    if request.method == 'POST':
        pic = Service_provider_pic_Form(request.POST, request.FILES)

        if pic.is_valid():
            pic.save()
            return render(request, 'user/user_profile.html')
        else:
            pic = Service_provider_pic_Form()

    return render(request, 'user/user_profile.html')


def delete_user_request_view(request, id = 0):
   
    service_requested = Request_service.objects.get(pk=id)

    service_requested.delete()

    service_view = Create_Service.objects.all()

    request_form = Request_ServiceForm()
    if request.method == 'POST':
        request_form = Request_ServiceForm(request.POST, request.FILES)

    if request_form.is_valid():
    #this saves the form
        request_form.save()
    # this refreshes the form
        return redirect('/user_dashboard')

    else:
        print("\n\n\n\n\n\n")
        print(request_form.errors)

    for i in request_form:
        print(i.label)
        print(i.errors)
    # dddd = service_view.id

    context = {
        'service_view': service_view,
        'request_form': request_form,
        # 'dddd': dddd,
    }
    
    return render(request,'user/user_dashboard_page.html', context)

    


# service provider section
def service_provider_dashboard_view(request):
    count_services = Create_Service.objects.all().count()
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
    
    context = {
        'form': form,
        'count_services': count_services,
    }

    return render(request, 'service_provider/service_provider_dashboard.html', context )


def all_services(request):
    display = Create_Service.objects.all()

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
    
    context = {
        'display': display,
        'form': form,
    }

    return render(request, 'service_provider/view_services.html', context)

# def service_provider_dashboard(request):

#     form = Create_ServiceForm()
#     if request.method == 'POST':
#         form = Create_ServiceForm(request.POST, request.FILES)
#         if form.is_valid():
            #this saves the form
            # form.save()
            # this refreshes the form
            # return redirect('/service_provider_dashboard')

        # else:
    #         print("\n\n\n\n\n\n")
    #         print(form.errors)
    #         for i in form:
    #             print(i.label)
    #             print(i.errors)
    
    # return render(request, 'service_provider/service_provider_dashboard.html', {'form':form})

def user_requests(request):
    #do this after you deal with the user requests section
    # count_user_request = 
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
    
    return render(request, 'service_provider/user_requests.html',{'form':form})

def service_provider_profile(request):
    if request.method == 'POST':
        pic = Service_provider_pic_Form(request.POST, request.FILES)

        if pic.is_valid():
            pic.save()
            return render(request, 'user/user_profile.html')
        else:
            pic = Service_provider_pic_Form()


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
    
    return render(request, 'service_provider/service_provider_profile.html', {'form':form})



def update_service_view(request, id ):
    obj= get_object_or_404(Post, id=id)
        
    form = Create_ServiceForm(request.POST or None, instance= obj)
    context= {'form': form}

    if form.is_valid():
        obj= form.save(commit= False)

        obj.save()

        messages.success(request, "You successfully updated the post")

        context= {'form': form}

        return render(request, 'posts/edit.html', context)

    else:
        context= {'form': form,
                  'error': 'The form was not updated successfully. Please enter in a title and content'}
        return render(request,'posts/edit.html' , context)






    
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
    
    
    return render(request, 'service_provider/service_provider_page.html', {'form':form})


def delete_service_view(request, id = 0):
   
    service_created = Create_Service.objects.get(pk=id)

    service_created.delete()
    return render(request,'service_provider/view_services.html')




def user_logout(request):
    logout(request)
    return redirect('main:home')

# # def form_view(request):
#     form = Create_ServiceForm()

#     # form = Create_ServiceForm()
#     if request.method == 'POST':
#         form = Create_ServiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             #this saves the form
#             form.save()
#             # this refreshes the form
#             return redirect('/service_provider_dashboard')

#         else:
#             print("\n\n\n\n\n\n")
#             print(form.errors)
#             for i in form:
#                 print(i.label)

#                 print(i.errors)

#     return render(request, 'service_provider/service_provider_dashboard.html')


# def unique_id():
#     u = 