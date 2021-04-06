from django.db import models
from django.contrib.auth.models import User
from parking.models import smartParking
# Create your models here.
	

class Inscriptions(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	numBadge =    models.CharField(max_length=30)
	phone=	      models.CharField(max_length=10)
	typeVoiture = models.CharField(max_length=30)
	matricule =   models.CharField(max_length=30)
	conditions =  models.BooleanField(default=True)
	parking = models.ForeignKey(smartParking, on_delete=models.CASCADE, null=True)
	entreprise = models.CharField(max_length=100, null=True)