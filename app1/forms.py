from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client , Adminstrateur , Voyage , Categorie , Hotel , Vol , Notification  , Promotion , Commentaire
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import Group
from django.forms import ModelForm

class ClientRegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]

    sexe = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    telephone = forms.IntegerField(
        # validators=[MinValueValidator(7), MaxValueValidator(15)]
    )
    adresse = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2', 'sexe', 'telephone', 'adresse']

    def save(self, commit=True): #had method an3yto liha f register view
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

            # Create a Client instance and associate it with the user
            client = Client.objects.create(
                fk_user=user,  # Use fk_user to associate with the User model
                sexe=self.cleaned_data['sexe'],
                telephone=self.cleaned_data['telephone'],
                adresse=self.cleaned_data['adresse'],
            )
        
        #hna kan associer user l group 'client'
        client_group = Group.objects.get(name='client')
        user.groups.add(client_group)
        return user






class AdminstrateurRegistrationForm(UserCreationForm):
    
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]

    sexe = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2', 'sexe']
    
    def save(self, commit=True): #had method an3yto liha f register view
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            
            user.is_staff = True
            user.is_superuser = True
            user.save()

            # Create an administrateur instance and associate it with the user
            administrateur = Adminstrateur.objects.create(
                fk_user=user,  # Use fk_user to associate with the User model
                sexe =self.cleaned_data['sexe'],
            )
        
        #hna kan associer user l group 'client'
        administrateur_group = Group.objects.get(name='admin')
        user.groups.add(administrateur_group)
        return user


class ClientSettingsForm(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
		exclude = ['fk_user']

class VoyageForm(ModelForm) : 
  class Meta :
    model = Voyage
    fields = '__all__'

class categorieForm(ModelForm) : 
  class Meta :
    model = Categorie
    fields = '__all__'

class hotelForm(ModelForm) : 
  class Meta :
    model = Hotel
    fields = '__all__'

class volForm(ModelForm) : 
  class Meta :
    model = Vol
    fields = '__all__'



class notificationForm(ModelForm) : 
  class Meta :
    model = Notification
    fields = '__all__'

    widgets = {
                'client': forms.TextInput(attrs={'readonly': 'readonly'}),
                'adminstrateur':forms.TextInput(attrs={'readonly': 'readonly'}),
            }


class promotionForm(ModelForm) : 
  class Meta :
    model = Promotion
    fields = '__all__'



class commentaireForm(ModelForm) : 
  class Meta :
    model = Commentaire
    fields = '__all__'
    widgets = {
            'client': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

