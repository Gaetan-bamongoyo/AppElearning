from django.db import models

# Create your models here.

class Module(models.Model):
    IdModule = models.AutoField(primary_key=True)
    module = models.CharField(max_length=50)
    montant = models.FloatField()
    description = models.TextField()
    detailcours = models.TextField(null=True)
    categorie = models.IntegerField(null=True)
    affecte = models.BooleanField(default=1)
    photo = models.ImageField(upload_to='module_photo')
    addDayDateAjout = models.DateField(auto_now_add=True)

class Categorie(models.Model):
    IdCategorie = models.AutoField(primary_key=True)
    categorie = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    addDayCategorie = models.DateField(auto_now_add=True)

class Contenus(models.Model):
    IdContenu = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    module = models.IntegerField(null=True)
    niveau = models.CharField(max_length=50, null=True)
    addDayContenu = models.DateField(auto_now_add=True)

class Inscription(models.Model):
    IdInscription = models.AutoField(primary_key=True)
    module = models.CharField(max_length=50)
    codemodule = models.IntegerField()
    niveau = models.CharField(max_length=50)
    montant = models.FloatField()
    etatpaiement = models.BooleanField(default=0)
    etatcours = models.IntegerField()
    user = models.IntegerField()

class Personne(models.Model):
    IdPersonne = models.AutoField(primary_key=True)
    user = models.TextField()
    identite = models.TextField(null=True)
    adresse = models.TextField(null=True)
    telephone = models.IntegerField(null=True)
    pays = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='user_photo')

class Video(models.Model):
    IdVideo = models.AutoField(primary_key=True)
    video = models.FileField(upload_to='video_cours', max_length=100)
    inscription = models.IntegerField()
    identite = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    formateur = models.IntegerField(default=2)


class Affectation(models.Model):
    IdAffectation = models.AutoField(primary_key=True)
    personne = models.IntegerField()
    module = models.IntegerField()
    addDayAjout = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='module_photo', null=True)
    modulename = models.CharField(max_length=50, null=True)
    
    
