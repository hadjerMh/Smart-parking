from django.shortcuts import render, redirect
from .models import Profil
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from parking.models import Reservation, smartParking
from .FormUser import CreateUserForm, UserUpdateForm
from django.contrib.auth.models import Group
from .decoraters import unauthenticated_user, allowed_users


@unauthenticated_user
def signUp(request):
	"""
	This function renders the User model in the sign up form page, onece the post request is submited
 	and the forme for the user creation is valide, the profile is created from the information gathered by the 
  	post request.
	"""
	#getting all the valid parkings
	queryset = smartParking.objects.all()
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			#create the user
			user = form.save()
			#getting or creating a group for customers so we can set access permissions
			group = Group.objects.get_or_create(name='customer')
			user.groups.add(group[0])
			#getting the input fields data from the post request
			username = form.cleaned_data.get('username')
			new_numBadge = request.POST.get('numBadge')
			new_phone = request.POST.get('phone')
			new_car = request.POST.get('car')
			new_numPlate = request.POST.get('numPlate')
			parking_company = request.POST.get('company')
			parking = smartParking.objects.get(compagnie_site=parking_company)
			print(parking_company)
			new_cdt = bool(request.POST.get('conditions'))
			print(new_cdt)
			#create the profil of the user
			Profil.objects.create(
				user=user,	
				numBadge = new_numBadge,
				phone = new_phone,
				typeCar = new_car, 
				numPlate = new_numPlate,
				conditions = new_cdt,
				company=parking_company,
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
	return render(request,"Inscription/signUp.html",context)
	
 
@unauthenticated_user
def loginView(request):
	""" This function allows the users to authetificate and loggin into the website and redirect the user 
 	to the parking home page or shows an info message so the user can correct the inserted values. 
	"""
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
	return render(request,"Inscription/login.html",{}) 


def logoutView(request):
	"""This function permit the user to logout and redirect him to the login page
	"""
	logout(request)
	return redirect('Connexion')


@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
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
	return render(request,'Inscription/updateUserInfo.html', context)
	

def globalHome(request):
	"""This function renders the home page
	"""
	return render (request, 'Inscription/globalHome.html',{})