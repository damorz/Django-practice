from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def IndexPage(request):
    context = {'name' : 'index'}
    return render(request , 'vue_app/index.html' , context=context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            elif username is not None and password != '' :
                messages.info(request,'Username or Password is incorrect.')
            else :
                messages.info(request,'Please fill your Username and Password.')
        context = {'name' : 'login'}
        return render(request,'vue_app/login.html',context=context)

def LogoutUser(request):
    logout(request)
    return redirect('login')

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = RegisterForm()
        if request.method == 'POST': #submit form
            form = RegisterForm(request.POST)
            print('waiting for saving . . .')

            if form.is_valid() and request.POST['first_name'] != '' and request.POST['last_name'] != '':
                print('saved user success!')
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

            else : 
                print('save error.')
        
        context={'name':'register','form':form }
        return render(request, 'vue_app/register.html' , context)

def TodoPage(request):
    context = {'name' : 'todo'}
    return render(request , 'vue_app/todo.html' , context=context)