from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Inscriptions

from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from parking.models import Reservation, smartParking
from .FormLs import CreateUserForm, UserUpdateForm
from django.contrib.auth.models import Group
from .decoraters import unauthenticated_user, allowed_users


# Create your views here.
@unauthenticated_user
def inscription_view(request):
	queryset = smartParking.objects.all()
	form=CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='customer')
			user.groups.add(group)
			username = form.cleaned_data.get('username')
			new_numBadge = request.POST.get('numBadge')
			new_phone = request.POST.get('phone')
			new_voiture = request.POST.get('voiture')
			new_matricule = request.POST.get('matricule')
			parking_entreprise = request.POST.get('entreprise')
			parking= smartParking.objects.get(compagnie_site=parking_entreprise)
			print(parking_entreprise)
			new_cdt = True	

			Inscriptions.objects.create(
				user=user,	
				numBadge = new_numBadge,
				phone = new_phone,
				typeVoiture = new_voiture, 
				matricule = new_matricule,
				conditions = new_cdt,
				entreprise=parking_entreprise,
				parking=parking,
				)
			Reservation.objects.create(user=user)
				
			messages.success(request,'Un compte a été créé pour '+ username)
			return redirect ('Connexion')
	context = {'form':form, 'parkings':queryset}	
	return render(request,"training.html",context)
	
@unauthenticated_user
def loginView(request):
	if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			print("user", user)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Votre nom d\'utilisateur ou mot de passe est incorrect')

		
	return render(request,"lg.html",{}) 

def logoutView(request):
	logout(request)
	return redirect('Connexion')

@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
	person = Inscriptions.objects.get(user=request.user)
	if request.method == 'POST':
	 	u_form = UserUpdateForm(request.POST, instance=request.user)
	 	new_phone = request.POST.get('phone')
	 	new_voiture = request.POST.get('voiture')
	 	new_matricule = request.POST.get('matricule')
	 	if u_form.is_valid():
	 		u_form.save()
	 		person = Inscriptions.objects.filter(user=request.user).update(phone=new_phone, typeVoiture=new_voiture, matricule=new_matricule)
	 		messages.success(request,'Votre profil a été modifié')
	 		return redirect('profil')
	else:
	 	u_form = UserUpdateForm(instance=request.user)
	 	
	context = {
	'u_form': u_form,
	'person' : person,
    }
	 
	return render(request,'user.html', context)
	
def bienvenue(request):
	return render (request, 'bienvenue.html',{})
	# if request.method == "POST":
	# 	new_nom = request.POST.get('nom')
	# 	new_prenom = request.POST.get('prenom')
	# 	
	# 	new_mail = request.POST.get('mail')
	# 	new_pw = request.POST.get('password')
	# 	#
	# 	new_cdt=True
	# 	print('notif', new_notif)
	# 	print(new_pw)
	# 	Inscriptions.objects.create(nom = new_nom, prenom = new_prenom, 
	# 	 	mail = new_mail, pw = new_pw, 
		