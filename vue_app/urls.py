from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', IndexPage, name='index'),
    path('login', LoginPage, name='login'),
    path('logout', LogoutUser, name='logout'),
    path('register', RegisterPage,name='register'),
    path('todo', TodoPage,name='todo'),
    path('admin', admin.site.urls)
]