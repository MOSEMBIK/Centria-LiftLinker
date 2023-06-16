# basic url mapping
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userindex, name='userindex'),
    path('settings/', views.usersettings, name='usersettings'),

    path('user/<str:username>', views.user, name='user'),
    path('search_user/', views.search_user, name='search_user'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('delete/', views.delete, name='delete'),
]