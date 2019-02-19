from django.db import models
from django.utils import timezone
from enum import Enum

class Agence(models.Model):
    nom_gerant = models.CharField(max_length=50)
    ville = models.CharField(max_length=65)
    tresorerie = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.ville

class Location(models.Model):
    agence = models.ForeignKey('Agence', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE)
    date_debut = models.DateTimeField(default=timezone.now, verbose_name="date du debut de la location")
    date_fin = models.DateTimeField(verbose_name="date de in de location")
    prix_final = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.id

class Client(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.nom

class Vehicule(models.Model):
    marque = models.CharField(max_length=20)
    modele = models.CharField(max_length=20)
    prix_loc = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.URLField()
    immatriculation = models.CharField(max_length=8, unique=True)

    choix_dispo = [('d','disponible'),('l','loué'),('m','en maintenance')]
    dispo = models.CharField(choices=choix_dispo, max_length=12)

    agence = models.ForeignKey('Agence', on_delete=models.CASCADE)

    choix_categorie = [('c','citadine'),('b','berline')]
    categorie = models.CharField(choices=choix_categorie, max_length=12)

    def __str__(self):
        return (self.marque, self.modele)