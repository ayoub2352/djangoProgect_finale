from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client
from django.core.validators import MinValueValidator, MaxValueValidator

class ClientRegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]

    sexe = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    telephone = forms.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)]
    )
    adresse = forms.CharField(max_length=100)
    CIN = forms.CharField(max_length=8)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2', 'sexe', 'telephone', 'adresse', 'CIN']

    def save(self, commit=True):
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
                CIN=self.cleaned_data['CIN'],
            )

        return user
