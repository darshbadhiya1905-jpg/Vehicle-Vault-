# parking/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Vehicle, ServiceBooking

@login_required
def dashboard(request):
    user = request.user
    context = {'role': user.get_role_display()}

    # 1. MANAGER WORKFLOW
    if user.is_manager:
        context['all_vehicles'] = Vehicle.objects.all()
        context['pending_tasks'] = ServiceBooking.objects.filter(status='Pending')
        context['active_staff'] = ServiceBooking.objects.exclude(status='Completed')
        return render(request, 'manager_dashboard.html', context)
    
    # 2. SERVICESTAFF WORKFLOW
    elif user.is_servicestaff:
        context['my_tasks'] = ServiceBooking.objects.filter(assigned_staff=user)
        return render(request, 'staff_dashboard.html', context)
    
    # 3. USER WORKFLOW
    else:
        context['my_vehicles'] = Vehicle.objects.filter(owner=user)
        context['my_bookings'] = ServiceBooking.objects.filter(vehicle__owner=user)
        return render(request, 'user_dashboard.html', context)
    
# Add this to the bottom of your Parking/views.py file

def adminDashboardView(request):
    # Fetch data for the Admin/Manager dashboard
    all_vehicles = Vehicle.objects.all()
    pending_tasks = ServiceBooking.objects.filter(status='Pending')
    
    context = {
        'all_vehicles': all_vehicles,
        'pending_tasks': pending_tasks,
    }
    
    # Renders the manager_dashboard.html template we created earlier
    return render(request, 'manager_dashboard.html', context)

def adminDashboardView(request):
    return render(request, 'admin_dashboard.html')

def userDashboardView(request):
    return render(request, 'user_dashboard.html')

def servicestaffDashboardView(request):
    return render(request, 'servicestaff_dashboard.html')