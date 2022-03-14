from django.db import models
from django.contrib.auth.models import User
from parking.models import smartParking


class Profil(models.Model):
	"""Profil class handels how the data of the inscription form for the simple users is stored in 
 		the database.

	Files:
		user: field with a one to one relationship with the standard authentification model User.
		numBadge: Character field, indicate the number of the badge with a maximum length of 30 characters.
		phone: Character field, indicate the phone number with a maximum length of 10 characters.
		typeVoiture: Character field, indicate the type of the car with a maximum length of 30 characters.
		matricule: Character field, indicate the numberplate of the car with a maximum length of 30 characters.
		conditions: Boolean field, indicate whether the user agrees with the policy of the website, 
  		default value is True.
		parking: Field with a one to many relationship with class smartParking on the parking/models.py.
		entreprise: Character Field, indicate the company with a max length of 100 characters.
	"""
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	numBadge = models.CharField(max_length=30)
	phone =	models.CharField(max_length=10)
	typeCar = models.CharField(max_length=30)
	numPlate = models.CharField(max_length=30)
	conditions = models.BooleanField(default=True)
	parking = models.ForeignKey(smartParking, on_delete=models.CASCADE, null=True)
	company = models.CharField(max_length=100, null=True)
	
	#Using the str function for a better visibility of the data in the django admin
	def __str__(self):
		return self.user.username + " " + self.parking.compagnie_site
