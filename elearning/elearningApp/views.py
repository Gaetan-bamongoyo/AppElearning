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
    module = Contenus.objects.filter(module=pk)
    context = {
        'module': module,
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
            return redirect('learning:module')

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


