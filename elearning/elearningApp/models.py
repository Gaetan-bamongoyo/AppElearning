from django.db import models

# Create your models here.

class Module(models.Model):
    IdModule = models.AutoField(primary_key=True)
    module = models.CharField(max_length=50)
    montant = models.FloatField()
    description = models.TextField()
    detailcours = models.TextField(null=True)
    categorie = models.IntegerField(null=True)
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
    
