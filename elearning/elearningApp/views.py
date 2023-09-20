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

def CertificatPage(request, pk):
    if request.user.is_authenticated:
        user_name = request.user.username
        personne = Personne.objects.get(user=user_name)
        inscription = Inscription.objects.get(IdInscription=pk)
        module = Module.objects.get(IdModule=inscription.codemodule)
        categorie = Categorie.objects.get(IdCategorie=module.categorie)
        user_name = Affectation.objects.get(module=inscription.codemodule)
        user_id = User.objects.get(id=user_name.personne)
        formateur = Personne.objects.get(user=user_id.username)
        context = {
            'identite': personne.identite,
            'module': module.module,
            'categorie': categorie.categorie,
            'formateur': formateur.identite
        }
        template = 'certificat.html'
        return render(request, template, context)

def ProfilPage(request):
    if request.user.is_authenticated:
        user_name = request.user.id
        user = User.objects.filter(id=user_name)
        cours = Inscription.objects.filter(user=user_name)
        utilisateur = User.objects.get(id=user_name)
        personne = Personne.objects.get(user=utilisateur.username)
        context = {
            'user':user,
            'cours':cours,
            'utilisateur': utilisateur.username,
            'photo': personne.photo,
            'identite': personne.identite,
            'adresse': personne.adresse,
            'phone': personne.telephone,
            'pays': personne.pays,
            'id':personne.IdPersonne
        }
        template = 'profil.html'
        return render(request, template, context)
# 
# creation de l'utilisateur
def CreateUser(request):
    user = User.objects.all()
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        identite = request.POST.get('identite')
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
                personne = Personne(
                    user=username,
                    photo='user_photo/10.jpg',
                    identite=identite
                )
                user.set_password(password)
                user.save()
                personne.save()
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

def CategoriePage(request):
    categorie = Categorie.objects.all()
    context = {
        'categorie': categorie
    }
    template = 'categorie.html'
    return render(request, template, context)

def ModulePage(request):
    module = Module.objects.all()
    categorie = Categorie.objects.all()
    context = {
        'module': module,
        'categorie': categorie
    }
    template = 'module.html'
    return render(request, template, context)

def ContenuModulePage(request, pk):
    module = Module.objects.filter(IdModule=pk)
    contenu = Contenus.objects.filter(module=pk)
    ids = Module.objects.get(IdModule=pk)
    idmodule = ids.IdModule
    context = {
        'module': module,
        'id': idmodule,
        'contenu': contenu
    }
    template = 'contenu.html'
    return render(request, template, context)

def CreateCategorie(request):
    if request.method=='POST':
        categorie = request.POST.get('categorie')
        description = request.POST.get('description')
        form = Categorie(
            categorie=categorie,
            description=description    
        )
        form.save()
        return redirect('learning:categorie')

def CreateContenu(request, pk):
    if request.method=='POST':
        titre = request.POST.get('titre')
        video = request.POST.get('video')
        niveau = request.POST.get('niveau')
        form = Contenus(
            titre=titre,
            video=video,
            module=pk,
            niveau=niveau
        )
        form.save()
        return redirect('learning:contenu', pk)

def CreateModule(request):
    if request.method=='POST':
        module = request.POST.get('module')
        description = request.POST.get('description')
        montant = request.POST.get('montant')
        categorie = request.POST.get('categorie')
        detailcours = request.POST.get('detailcours')
        photo = request.FILES.get('photo')
        form = Module(
            montant=montant,
            photo=photo,
            description=description,
            module=module,
            categorie=categorie,
            detailcours=detailcours
        )
        form.save()
        return redirect('learning:module')

def CreateUserAdmin(request):
    user = User.objects.all()
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        identite = request.POST.get('identite')
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
            personne = Personne(
                    user=username,
                    photo='user_photo/10.jpg',
                    identite=identite
            )
            personne.save()
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
    categorie = Categorie.objects.all()
    context = {
        'module': module,
        'categorie': categorie
    }
    template = 'course.html'
    return render(request, template, context)

def CoursDetailPage(request, pk):
    module = Module.objects.get(IdModule=pk)
    categorie = Categorie.objects.all()
    img = module.photo 
    detail = module.detailcours
    contenu = Contenus.objects.filter(module=pk)
    context = {
        'module': module,
        'categorie': categorie,
        'img':img,
        'detail':detail,
        'contenu': contenu
    }
    template = 'coursedetail.html'
    return render(request, template, context)

def UniqueCoursPage(request, pk):
    module = Module.objects.filter(categorie=pk)
    categorie = Categorie.objects.all()
    context = {
        'module': module,
        'categorie': categorie
    }
    template = 'courseUnique.html'
    return render(request, template, context)

# 
# 
# 
# 
def InscriptionPage(request, pk):
    module = Module.objects.filter(IdModule=pk)
    context = {
        'module': module,
    }
    template = 'inscription.html'
    return render(request, template, context) 

def MesCoursLirePage(request, pk):
    etat = Inscription.objects.get(IdInscription=pk)
    module = Contenus.objects.filter(module=etat.codemodule)
    context = {
        'module': module,
        'etat': etat.etatcours,
        'id': pk
    }
    template = 'contenudetail.html'
    return render(request, template, context)

def CreateInscription(request, pk):
    if request.method=='POST':
        niveau = request.POST.get('niveau')
        module = Module.objects.get(IdModule=pk)
        if request.user.is_authenticated:
            user_name = request.user.id
            form = Inscription(
                niveau=niveau,
                codemodule=pk,
                etatcours=0,
                module=module.module,
                montant=module.montant,
                user=user_name
            )
            form.save()
            return redirect('learning:mescours')

def PaiementPage(request, pk):
    module = Inscription.objects.get(IdInscription=pk)
    ids = module.IdInscription
    montant = module.montant
    context = {
        'id': ids,
        'montant': montant
    }
    template = 'paiement.html'
    return render(request, template, context)

def CreatePaiement(request, pk):
    if request.method=='POST':
        inscription = Inscription.objects.get(IdInscription=pk)
        form = Inscription(
            IdInscription=pk,
            module=inscription.module,
            codemodule=inscription.codemodule,
            etatcours=inscription.etatcours,
            etatpaiement=1,
            montant=inscription.montant,
            niveau=inscription.niveau,
            user=inscription.user
        )
        form.save()
        return redirect('learning:mescours')

# 
# 
#
def MesCoursPage(request):
    if request.user.is_authenticated:
        user_name = request.user.id
        module = Inscription.objects.filter(user=user_name)
        context = {
            'module': module,
        }
        template = 'mescours.html'
        return render(request, template, context)

def CreatePersonne(request):
    if request.method=='POST':
        user = request.POST.get('user')
        identite = request.POST.get('identite')
        adresse = request.POST.get('adresse')
        pays = request.POST.get('pays')
        phone = request.POST.get('phone')
        ids = request.POST.get('id')
        photo = request.FILES.get('photo')
        form = Personne(
            adresse=adresse,
            identite=identite,
            pays=pays,
            telephone=phone,
            user=user,
            photo= photo,
            IdPersonne=ids
        )
        form.save()
        return redirect('learning:profil')

# 
# 
# 
#  operation Affectation
# 
# 
#

def ListeCoursePage(request):
    if request.user.is_authenticated:
        user_name = request.user.id
        affectation = Affectation.objects.filter(personne=user_name)
        context = {
                'affectation': affectation,
            }
        template = 'listecourse.html'
        return render(request, template, context) 
 
def AffectationPage(request, pk):
    module = Module.objects.get(IdModule=pk)
    user = User.objects.filter(is_staff=0)
    context = {
            'id': module.IdModule,
            'user': user
        }
    template = 'affectation.html'
    return render(request, template, context) 

def CreateAffectation(request, pk):
    if request.method=='POST':
        user = request.POST.get('user')
        module = Module.objects.get(IdModule=pk)
        form = Affectation(
            module=pk,
            personne=user,
            modulename=module.module,
            photo=module.photo
        )
        module = Module(
            IdModule=pk,
            module=module.module,
            addDayDateAjout=module.addDayDateAjout,
            categorie=module.categorie,
            affecte=0,
            description=module.description,
            detailcours=module.detailcours,
            montant=module.montant,
            photo=module.photo
        )
        module.save()
        form.save()
        return redirect('learning:module')
# 
# 
# 
# configuration video (CRUD)
# 
# 
# 
def VideoLien(request, pk):
    context = {
            'id': pk
        }
    template = 'examen.html'
    return render(request, template, context) 

def VideoListe(request):
    if request.user.is_authenticated:
        user_name = request.user.id
        video = Video.objects.filter(formateur=user_name)
        context = {
                'video': video
            }
        template = 'validevideo.html'
        return render(request, template, context) 

def VideoLireValide(request, pk):
    video = Video.objects.get(IdVideo=pk)
    inscription = Inscription.objects.get(IdInscription=video.inscription)
    context = {
            'video': video.video,
            'id': video.inscription,
            'etat': inscription.etatcours
        }
    template = 'lirevideo.html'
    return render(request, template, context)

def CreateVideo(request, pk):
    if request.method=='POST':
        video = request.FILES.get('video')
        inscription = Inscription.objects.get(IdInscription=pk)
        affectation = Affectation.objects.get(module=inscription.codemodule)
        # user = Personne.objects.get(user=inscription.user)
        form = Video(
            inscription=pk,
            module=inscription.codemodule,
            video= video,
            identite=video,
            formateur=affectation.formateur
        )
        form.save()
        return redirect('learning:mescours')
    
def CreateValideVideo(request, pk):
    inscription = Inscription.objects.get(IdInscription=pk)
    form = Inscription(
            IdInscription=pk,
            module=inscription.module,
            codemodule=inscription.codemodule,
            etatcours=1,
            etatpaiement=1,
            montant=inscription.montant,
            niveau=inscription.niveau,
            user=inscription.user,
        )
    form.save()
    return redirect('learning:listevideo')




