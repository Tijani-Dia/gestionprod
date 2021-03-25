from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

class User(AbstractUser):
    """
    User Model 
    """
    ROLE_CHOICES = [
        ('A', 'Administrateur'),
        ('Q', 'Contrôleur Qualité'),
        ('P', 'Contrôleur Production'),
        ('C', 'Contrôleur Chargement'),
        ('M', 'Mainteneur'),
    ]

    user_role = models.CharField(choices=ROLE_CHOICES, unique=True, max_length=1)

    USERNAME_FIELD = "user_role"
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.username

class Formulaire(models.Model):
    """ 
    Parent class from which all formModels will
    inherit from. 
    """
    controleur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    observation = models.TextField(blank=True)
