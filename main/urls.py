# basic url mapping
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('s/', views.search, name='search'),
    path('a/', views.about, name='about'),
]
