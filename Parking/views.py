from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login") #check in core.urls.py login name should exist..
def adminDashboardView(request):
    return render(request,"parking/admin_dashboardview.html")

@login_required(login_url="login") #check in core.urls.py login name should exist..
def userDashboardView(request):
    return render(request,"parking/user_dashboardview.html")

@login_required(login_url="login") #check in core.urls.py login name should exist..
def servicestaffDashboardView(request):
    return render(request,"parking/servicestaff_dashboardview.html")