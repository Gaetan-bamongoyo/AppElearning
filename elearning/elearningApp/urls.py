from django.urls import path
from .views import *

app_name = 'learning'
urlpatterns = [
    path('', LoginPage, name='login'),
    path('register', RegisterPage, name='register'),
    path('home', Dashboard, name='home'),
    path('logout', LogoutUser, name='logout'),
    
    # 
    # operation connection CRUD
    # 
    path('create', CreateUser, name='create'),
    path('signin', loginUser, name='signin'),
    
    # 
    # 
    path('setting', SettingPage, name='setting'),
    path('module', ModulePage, name='module'),
    path('createuser', CreateUserAdmin, name='createuser'),
    path('createmodule', CreateModule, name='createmodule'),
    # 
    # 
    # 
    path('course', CoursPage, name='course'),
]
