from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    imagenPerfil =models.ImageField(upload_to= 'avatares', null=True, default = 'PorDefecto/profileImageDefault.jpg')