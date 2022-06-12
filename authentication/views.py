from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
# from django.contrib.auth.models import *
from django.db import IntegrityError
from .models import *


# Create your views here.

# login user view which authenticate the user
def login_user_view(request):

    if request.method == "POST":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username = username , password = password)
        print(user)

        
        if user.is_user == True:
            login(request, user)
            return redirect("main:user_dashboard")

        elif user.is_service_provider == True:
            login(request, user)
            return redirect("main:service_provider_dashboard")

        elif username =="admin":
            return redirect("dashboard:admin_dashboard")

        else:
            return HttpResponse("try again")

    return render(request,'login/login_user.html')


# register user view which saves the user details in the data base
def register_user_view(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        get_level = request.POST['user']
       
       # this deals with the radio button selection
        if get_level == 'User':

            user = MyData.objects.create(
                username = username,
                email = email,
                is_user = True
            )
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("yes is user")

        elif get_level == 'Service_Provider':
            user = MyData.objects.create(
                username = username,
                email = email,
                is_service_provider = True
            )
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("yes is service")
        user.set_password(password)
        user.save()

        return redirect("auth:user_authentication")

    else:
        pass
    return render(request,'register/signup_user.html')








# this function checks the data abse and authenticate the user to display its page

# def login_service_provider_view(request):

#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username , password = password)
#         if user == None:
#             # return HttpResponse("masa go and sleep")
#             return HttpResponse("try again")

#         elif username =="admin":
#             return redirect("dashboard:admin_dashboard")
            
#         else:
#             login(request, user)
#             return redirect("main:service_provider_dashboard")
#     return render(request,'login/login_service_provider.html')
    

# this function authenticates and sends data fromt he front end to the back end/database
# def register_service_provider_view(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         user = MyData.objects.create(
#             username = username,
#             email = email,
#             is_service_provider = True
#         )
        
#         user.set_password(password)
#         user.save()

       
#         return redirect("auth:service_provider_login")

#     else:
#         pass

#     return render(request,'login/login_service_provider.html')


# def logout_view(request):
#     logout(request)
#     return redirect('main:home')



# def register_user_view(request):
#     forms = UserRegForm()
#     if request.method == 'POST':
        
#         # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#         # print(request.POST)

#         data_username = User.objects.filter(username = username).first
#         try:
#             user = User.objects.create(
#                 username = username,
#                 email = email,
#             )
#             user.set_password(password)
#             user.save()
#         except IntegrityError as e: 
#                 return HttpResponse("sdfasdfaskdhsajdfhksdf")

#         # return redirect("auth:user_login")
#         return HttpResponse("Ok its working")

#     else:
#         pass

#     context ={
#         'forms':forms
#     }
#     return render(request,'login/login_user.html',context)
     
     
# def register_view(request):
#     next = request.GET.get('next')
#     form = UserRegisterForm(request.POST or None)
#     if forms.is_valid():
#         user = form.save(commit = False)
#         password = form.cleaned_data.get("password")
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username =username, password=password)
#         login(request, new_user)
#         if next:
#             return redirect(next)
#         return redirect("/")

#     context = {
#         'form': form,
#     }
#     return render(request, "register/register_user.html", context)


# def user_login(request):
   
#     return render(request,'login/login_user.html')

# def service_provider_login(request):

#     return render(request,'login/login_service_provider.html')


# def user_registeration(request):
   
#     return render(request,'register/register_user.html')


# def service_provider_registeration(request):
   
#     return render(request,'register/register_service_provider.html')

# Create your views here.
