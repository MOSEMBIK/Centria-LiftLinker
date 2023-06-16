# basic url mapping
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('n/', views.news, name='news'),
    path('p/', views.places, name='places'),

    path('a/a', views.about, name='about'),
    path('a/c', views.aboutcontact, name='aboutcontact'),
    
]
