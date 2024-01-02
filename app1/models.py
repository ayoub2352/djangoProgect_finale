from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Client(models.Model):
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES =[
        ('F','Female'),
        ('M','Male')
    ]
    sexe = models.CharField(choices=GENDER_CHOICES,max_length=1)
    telephone = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(10)
        ]
    )
    adresse = models.CharField(max_length=100)
    CIN = models.CharField(max_length=8)
    solde = models.IntegerField(default=0)

class voyage(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_depart = models.DateField()
    date_arrivee = models.DateField()
    prix = models.IntegerField()
    nbr_places = models.IntegerField()
    # image = models.ImageField(upload_to='images/')
    