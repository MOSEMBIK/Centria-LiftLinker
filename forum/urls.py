# basic url mapping
from django.urls import path
from . import views

urlpatterns = [
    path('', views.forumindex, name='forumindex'),
    path('post/<int:postID>', views.post, name='post'),
    path('newpost/', views.newpost, name='newpost'),
]