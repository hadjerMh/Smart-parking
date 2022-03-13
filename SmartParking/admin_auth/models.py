from django.db import models
from django.contrib.auth.models import User


class admin_profil(models.Model):
	"""admin_profil class handels how the data of the admin users is stored in the database.

	Files:
		admin_person: field with a one to one relationship with the standard authentification model User.
		phone: Character field, indicate the phone number with a maximum length of 10 characters.
		conditions: Boolean field, indicate whether the user agrees with the policy of the website.
		entreprise: Character Field, indicate the company with a max length of 100 characters.
		address_entreprise: Character Field, indicate the company address, with a max length of 250 characters.
	"""
	admin_person = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	phone =	models.CharField(max_length=10, verbose_name="Numéro de téléphone: ")
	entreprise = models.CharField(max_length=100, verbose_name="Nom de votre entreprise: ")
	adress_entreprise = models.CharField(max_length=250, verbose_name="Adresse de l'entreprise: ")
	conditions =  models.BooleanField(default=True)
 
	def __str__(self):
		return self.admin_person.username + " " + self.entreprise
	