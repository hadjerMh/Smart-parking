from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class admin_profil(models.Model):
	admin_person = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	phone =	     models.CharField(max_length=10,  verbose_name="Numéro de téléphone: ")
	entreprise = models.CharField(max_length=100,  verbose_name="Nom de votre entreprise: ")
	adress_entreprise = models.CharField(max_length=250,  verbose_name="Adresse de l'entreprise: ")
	conditions =  models.BooleanField(default=True)
	