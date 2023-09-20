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
    path('profil', ProfilPage, name='profil'),
    path('personne', CreatePersonne, name='personne'),
    path('certificat/<int:pk>', CertificatPage, name='certificat'),
    
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
    path('affectation/<int:pk>', AffectationPage, name='affectation'),
    path('createaffectation/<int:pk>', CreateAffectation, name='createaffectation'),
    path('mescours', MesCoursPage, name='mescours'),
    path('listecourse', ListeCoursePage, name='listecourse'),
    path('paiement/<int:pk>', PaiementPage, name='paiement'),
    path('createpaiement/<int:pk>', CreatePaiement, name='createpaiement'),
    
    # 
    # 
    # 
    # 
    path('examen/<int:pk>', VideoLien, name='examen'),
    path('addvideo/<int:pk>', CreateVideo, name='addvideo'),
    path('listevideo', VideoListe, name='listevideo'),
    path('valide/<int:pk>', CreateValideVideo, name='valide'),
    path('lirevideo/<int:pk>', VideoLireValide, name='lirevideo'),
    # 
    # 
    # 
    # 
    path('inscription/<int:pk>', InscriptionPage, name='inscription'),
    path('createinscription/<int:pk>', CreateInscription, name='createinscription'),
]
