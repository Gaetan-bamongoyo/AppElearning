from django.db import models

# Create your models here.

class Module(models.Model):
    IdModule = models.AutoField(primary_key=True)
    module = models.CharField(max_length=50)
    montant = models.FloatField()
    description = models.TextField()
    photo = models.ImageField(upload_to='module_photo')
    addDayDateAjout = models.DateField(auto_now_add=True)
