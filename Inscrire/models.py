from django.db import models

# Create your models here.

class Etudiant(models.Model):
     nom= models.CharField(max_length=200)
     photoEtudiant=models.ImageField(null=True)
     nni=models.IntegerField()
     sexe=models.CharField(max_length=200)
     dateNaissance=models.DateField()
     lieuNaissance= models.CharField(max_length=200)
     telephone = models.CharField(max_length=200)
     email = models.CharField(max_length=200)
     carteIdentite=models.ImageField(null=True)
     numBac=models.IntegerField()
     serie= models.CharField(max_length=200)
     releveNote=models.ImageField(null=True)
     session= models.CharField(max_length=200)
     moyenGeneral=models.FloatField()
     pays= models.CharField(max_length=200)
     AnObtantionBac=models.DateField()
     niveau=models.CharField(max_length=200, null=True)

     def __str__(self):  
        return self.nom