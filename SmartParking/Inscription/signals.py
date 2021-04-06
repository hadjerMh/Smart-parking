from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Inscriptions
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
    	
		# new_numBadge = request.POST.get('numBadge')
		# new_phone = request.POST.get('phone')
		# new_voiture = request.POST.get('voiture')
		# new_matricule = request.POST.get('matricule')
		# parking_entreprise = request.POST.get('entreprise')
		# print(parking_entreprise)
		# new_cdt = True	

		# Inscriptions.objects.create(
		# 	user=instance,	
		# 	numBadge = new_numBadge,
		# 	phone = new_phone,
		# 	typeVoiture = new_voiture, 
		# 	matricule = new_matricule,
		# 	conditions = new_cdt,
		# 	entreprise=parking_entreprise,
		# 	)
		
		print('user created')
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.Inscriptions.save()