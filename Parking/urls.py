from django.urls import path
from . import views

urlpatterns = [

    path('admin-dashboard/', views.adminDashboardView, name='admin_dashboard'),

    path('user-dashboard/', views.userDashboardView, name='user_dashboard'),

    path('servicestaff-dashboard/', views.servicestaffDashboardView, name='servicestaff_dashboard'),

]