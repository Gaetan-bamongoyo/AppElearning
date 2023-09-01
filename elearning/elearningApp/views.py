from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.template import loader
from .models import *
# login import
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def LoginPage(request):
    template = 'login.html'
    return render(request, template)

def RegisterPage(request):
    template = 'register.html'
    return render(request, template)

def Dashboard(request):
    template = 'dashboard.html'
    return render(request, template)
# 
# creation de l'utilisateur
def CreateUser(request):
    user = User.objects.all()
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exits')
                return redirect('learning:register')
            else:
                user = User(
                        username=username,
                        password=password,
                        email=email,
                        is_staff=1
                )
                user.set_password(password)
                user.save()
                return redirect('learning:login')
                    
    else:
        return redirect('learning:register')
    return render(request, '')


def loginUser(request):
    # template = 'login.html'
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')       
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('learning:home')
        else:
            return redirect('learning:login')
    else:
        return render(request, '')


def LogoutUser(request):
    auth.logout(request)
    return redirect('learning:login')

# 
# 
# partie administrateur
# 
# 

def SettingPage(request):
    user = User.objects.all()
    context = {
        'user': user
    }
    template = 'setting.html'
    return render(request, template, context)

def ModulePage(request):
    module = Module.objects.all()
    context = {
        'module': module
    }
    template = 'module.html'
    return render(request, template, context)

def CreateModule(request):
    if request.method=='POST':
        module = request.POST.get('module')
        description = request.POST.get('description')
        montant = request.POST.get('montant')
        photo = request.FILES.get('photo')
        form = Module(
            montant=montant,
            photo=photo,
            description=description,
            module=module
        )
        form.save()
        return redirect('learning:module')

def CreateUserAdmin(request):
    user = User.objects.all()
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        isstaff = request.POST.get('isstaff')
        
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exits')
                return redirect('learning:setting')
        else:
            user = User(
                        username=username,
                        password=password,
                        email=email,
                        is_staff=0,
                        is_superuser=isstaff
                )
            user.set_password(password)
            user.save()
            return redirect('learning:setting')
                    
    else:
        return redirect('learning:setting')
    return render(request, '')


# 
# 
# Partie cliente
# 
# 
# 
def CoursPage(request):
    module = Module.objects.all()
    context = {
        'module': module
    }
    template = 'course.html'
    return render(request, template, context)

