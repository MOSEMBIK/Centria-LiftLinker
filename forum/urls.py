# basic url mapping
from django.urls import path
from . import views

urlpatterns = [
    path('', views.forumindex, name='forumindex'),
]