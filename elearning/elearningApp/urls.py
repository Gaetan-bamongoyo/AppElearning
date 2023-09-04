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
    path('categorie', CategoriePage, name='categorie'),
    path('contenu/<int:pk>', ContenuModulePage, name='contenu'),
    path('createcontenu/<int:pk>', CreateContenu, name='createcontenu'),
    path('createcategorie', CreateCategorie, name='createcategorie'),
    path('createuser', CreateUserAdmin, name='createuser'),
    path('createmodule', CreateModule, name='createmodule'),
    # 
    # 
    # 
    path('course', CoursPage, name='course'),
    path('coursedetail/<int:pk>', CoursDetailPage, name='coursedetail'),
    path('getcours/<int:pk>', UniqueCoursPage, name='getcours'),
    path('contenudetail/<int:pk>', MesCoursLirePage, name='contenudetail'),
    path('mescours', MesCoursPage, name='mescours'),
    path('paiement/<int:pk>', PaiementPage, name='paiement'),
    path('createpaiement/<int:pk>', CreatePaiement, name='createpaiement'),
    # 
    # 
    # 
    # 
    path('inscription/<int:pk>', InscriptionPage, name='inscription'),
    path('createinscription/<int:pk>', CreateInscription, name='createinscription'),
]
