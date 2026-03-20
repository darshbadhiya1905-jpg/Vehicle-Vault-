from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def login_page(request):
    return render(request,'core/login.html')

def dashboard(request):
    return render(request,'core/dashboard.html')

def vehicles(request):
    return render(request,'core/vehicles.html')

def services(request):
    return render(request,'core/services.html')