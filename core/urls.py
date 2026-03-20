from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # 👈 THIS IS MAIN PAGE
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
]