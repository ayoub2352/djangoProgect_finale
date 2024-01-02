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
    # client_image = models.ImageField(upload_to='images/')

class Voyage(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_depart = models.DateField()
    date_arrivee = models.DateField() 
    prix = models.IntegerField(null=False, blank=False)#🚩here can be blank because it's only admin tasks , it can be that the admin dont know yet the price of the voyage
    nbr_places = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(10)
        ]
    )
    # image_voyage = models.ImageField(upload_to='images/')

class Client_voyage(models.Model):
    fk_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fk_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    date_reservation = models.DateField()