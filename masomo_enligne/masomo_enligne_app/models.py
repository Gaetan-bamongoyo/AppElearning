from django.db import models

# Create your models here.

class Personne(models.Model):
    IdPersonne = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    date = models.DateTimeField( auto_now=False, auto_now_add=True)
