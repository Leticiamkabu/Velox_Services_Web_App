from django.shortcuts import render, HttpResponse


# Create your views here.
def admin_dashboard_view(request):
    return render(request, 'admin/main_admin_dashboard.html')
    

def testing(request):
    return render(request, "base/base.html")