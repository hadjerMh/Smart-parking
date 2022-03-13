from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from admin_auth.models import admin_profil


class smartParking(models.Model):
	"""smartParking

	Args:
		models (_type_): _description_

	Returns:
		_type_: _description_
	"""
	compagnie_site = models.CharField(max_length=100, null=True)
	administ = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	numPlaces = models.PositiveSmallIntegerField(default=30)
	reserveDuration = models. DurationField(default=timedelta(minutes=20))
	parking_latitude = models.CharField(max_length=30, null=True)
	parking_longitude = models.CharField(max_length=30, null=True)
	distance = models.CharField(max_length=10, default=1)

	def __str__(self):
		return self.compagnie_site + " " + str(self.numPlaces)
 
 
class Reservation(models.Model):
	"""_summary_

	Args:
		models (_type_): _description_

	Returns:
		_type_: _description_
	"""
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="utilisateur")
	R =  models.BooleanField(default=False , verbose_name="reserve") #résarvation
	arrived = models.BooleanField(default=False, verbose_name="arrive")
	number_reservation = models.PositiveSmallIntegerField(default=0)
	scan_entre = models.BooleanField(default=False, verbose_name="scanEntre")
	scan_out = models.BooleanField(default=False, verbose_name="scanSortie")
	timeout = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id)


class State(models.Model):
	"""_summary_

	Args:
		models (_type_): _description_

	Returns:
		_type_: _description_
	"""
	placeName = models.CharField(max_length=10) #number of the place
	place_given_name = models.CharField(max_length=10, null=True, blank=True)
	statePlace = models.BooleanField(default=False) #pour la demonstration seulement changer editable a true
	parking = models.ForeignKey(smartParking, on_delete=models.CASCADE, default=1)
	user = models.ForeignKey(User, models.SET_NULL, null = True, blank= True)
 
	def __str__(self):
		return str(self.placeName) + " " + str(self.statePlace)
	

class Reclamation(models.Model):
	"""_summary_

	Args:
		models (_type_): _description_

	Returns:
		_type_: _description_
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Utilisateur")
	parking = models.ForeignKey(smartParking, on_delete=models.CASCADE, null=True)
	site = 'un problème au niveau du site'
	probparking = 'une infraction au niveau du parking'
	autre ="autre"
	choices_rec = [
 		( site, 'un problème au niveau du site'),
		(probparking , 'une infraction au niveau du parking'),
		( autre, 'autre'),
	]
	choice = models.CharField(max_length=100, choices = choices_rec, default=site, verbose_name="Mon problème")
	rec_text = models.TextField(null=True, blank=True, verbose_name="Décrivez votre problème")
	pic = models.ImageField(null=True, blank=True, verbose_name="insertion d'une image ou capture d'écran")

	def __str__(self):
		return self.user.username + " " + self.choice