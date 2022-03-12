from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil




class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label = 'Contraseña', widget= forms.PasswordInput)
    password2=forms.CharField(label = 'Repetir contraseña', widget= forms.PasswordInput)
    first_name=forms.CharField()
    last_name=forms.CharField()
    

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2','first_name','last_name']

class UserEditionForm(UserCreationForm):
    email= forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    imagenPerfil= forms.ImageField()
    

    class Meta:
        model=User
        fields=[ 'email', 'password1', 'password2','first_name','last_name','imagenPerfil']

class PerfilForm(forms.ModelForm):
    imagenPerfil= forms.ImageField(required=False, widget=forms.FileInput)
    
    class Meta:
        model = Perfil
        fields = ['imagenPerfil']
        
