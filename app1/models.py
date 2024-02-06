from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Client(models.Model):
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES =[
        ('F','Female'),
        ('M','Male')
    ]
    sexe = models.CharField(choices=GENDER_CHOICES,max_length=1)
    telephone = models.IntegerField(
    #    validators=[  
        # MinLengthValidator(9),
        # MaxLengthValidator(15)
        # ]
    )
    adresse = models.CharField(max_length=100)
    client_image = models.ImageField(default = "profilepic.png",null=True , blank=True)
    def __str__(self) : 
     return self.fk_user.username

class Categorie(models.Model):
    nom = models.TextField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    categorie_image = models.ImageField(default = "voyagepic.png",null=True , blank=True)
    def __str__(self) : 
     return self.nom

class Promotion(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    pourcentage_reduction = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])


    def _str_(self):
        return self.titre


class Hotel(models.Model):
    nom = models.TextField(max_length=100)
    NBR_ETOILE = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    nbr_etoiles = models.IntegerField(choices=NBR_ETOILE, null=False, blank=False)
    nbr_chambres = models.IntegerField(null=False, blank=False)
    hotel_image = models.ImageField(default = "hotel.jpeg",null=True , blank=True)
    def __str__(self):
        return self.nom


class Vol(models.Model) : 
    id = models.AutoField(primary_key=True) 
    titre = models.CharField(max_length=100,default='titre1')
    date_depart = models.DateField(null=False , blank=False)
    date_arrive = models.DateField(null=False,blank=False)
    compagnie = models.CharField(null=False , blank=False , max_length=100)
    CLASSE_CHOICES =[
        ('eco','economie'),
        ('bsn','bisness')
    ]
    classe = models.CharField(choices=CLASSE_CHOICES,null=False, blank=False ,max_length=100)
    escale = models.CharField(max_length=100 ,null=False , blank=False)
    ville_arrive = models.CharField(max_length=100 ,null=False , blank=False)
    ville_depart = models.CharField(max_length=100 ,null=False , blank=False)
    nbr_heure = models.IntegerField(null=False, blank=False)
    
    def __str__(self) : 
        return self.titre


class Voyage(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_depart = models.DateField()
    date_arrivee = models.DateField() 
    prix = models.IntegerField(null=False, blank=False)#🚩here can be blank because it's only admin tasks , it can be that the admin dont know yet the price of the voyage
    nbr_places = models.IntegerField(null=False, blank=False)  #7ydt validators 7it daro liya mochkil
    image_voyage = models.ImageField(default = "voyagepic.png",null=True , blank=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE )
    promotion = models.ForeignKey('Promotion', null=True,blank=True, on_delete=models.CASCADE)
    vol = models.ForeignKey('Vol',on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel',on_delete=models.CASCADE)
    def __str__(self) : 
     return self.titre

class Client_voyage(models.Model):
    fk_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fk_voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    date_reservation = models.DateField()
    amountPaid = models.IntegerField(null=False, blank=False,default=0)
    paymentStatus = models.BooleanField(default=False)


class Adminstrateur(models.Model):
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES =[
        ('F','Female'),
        ('M','Male')
    ]
    sexe = models.CharField(choices=GENDER_CHOICES,max_length=1)
    
    def __str__(self) : 
     return self.fk_user.username



class Notification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    adminstrateur = models.ForeignKey(Adminstrateur, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adminstrateur.fk_user.username} to {self.client.fk_user.username}: {self.message}"

class Commentaire(models.Model) : 
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    commentaire = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.client.fk_user.username}: {self.commentaire} at : {self.timestamp}"
