from django.shortcuts import render, redirect
from .models import Profil
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from parking.models import Reservation, smartParking
from .FormLs import CreateUserForm, UserUpdateForm
from django.contrib.auth.models import Group
from .decoraters import unauthenticated_user, allowed_users


@unauthenticated_user
def inscription_view(request):
	queryset = smartParking.objects.all()
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			#create the user
			user = form.save()
			#Puting the user in the right group for the right group 
			group = Group.objects.get(name='customer')
			user.groups.add(group)
			#getting the input fields data from the post request
			username = form.cleaned_data.get('username')
			new_numBadge = request.POST.get('numBadge')
			new_phone = request.POST.get('phone')
			new_car = request.POST.get('car')
			new_numPlate = request.POST.get('numPlate')
			parking_company = request.POST.get('entreprise')
			parking = smartParking.objects.get(compagnie_site=parking_company)
			print(parking_company)
			new_cdt = True	
			#create the profil of the user
			Profil.objects.create(
				user=user,	
				numBadge = new_numBadge,
				phone = new_phone,
				typeCar = new_car, 
				matricule = new_numPlate,
				conditions = new_cdt,
				entreprise=parking_company,
				parking=parking,
				)
			#create a reservation instance for the user
			Reservation.objects.create(user=user)
			#creating a success message
			messages.success(request,'Un compte a été créé pour '+ username)
			#redirecting to the login page
			return redirect ('Connexion')
	context = {
     		'form':form,
       		'parkings':queryset
        	}
	return render(request,"Inscription/inscription.html",context)
	
@unauthenticated_user
def loginView(request):
	if request.method == 'POST':
			#get the username and the password from the POST request
			username = request.POST.get('username')
			password =request.POST.get('password')
			#use the function authenticate to authenticate the user
			user = authenticate(request, username=username, password=password)
			print("user", user)
			#checking if th euser exists
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				#creating an info message to informe the user given 
				messages.info(request, 'Votre nom d\'utilisateur ou mot de passe est incorrect')		
	return render(request,"Inscription/lg.html",{}) 


def logoutView(request):
	logout(request)
	return redirect('Connexion')


@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
	person = Profil.objects.get(user=request.user)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user) 
		new_phone = request.POST.get('phone')
		new_car = request.POST.get('car')
		new_numPlate = request.POST.get('numPlate')
		if u_form.is_valid():
			u_form.save()
			person = Profil.objects.filter(user=request.user).update(phone=new_phone, typeCar=new_car, numPlate=new_numPlate)
			messages.success(request,'Votre profil a été modifié')
			return redirect('profil')
	else:
		u_form = UserUpdateForm(instance=request.user)
	context = {
			  'u_form': u_form,
			  'person' : person
    		}
	return render(request,'Inscription/user.html', context)
	
 
def bienvenue(request):
	return render (request, 'Inscription/bienvenue.html',{})