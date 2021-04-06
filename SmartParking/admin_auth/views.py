from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import admin_profil
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import CreateUserForm, Create_admin_profil, UserUpdateForm, ProfilUpdate
from django.forms import inlineformset_factory
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from parking.models import smartParking, State, Reclamation
from datetime import timedelta
from Inscription.decoraters import allowed_users
from Inscription.models import Inscriptions
from django.contrib import messages

# Create your views here.
@unauthenticated_user
def admin_inscription (request):
	user_form = CreateUserForm()
	profil_form = Create_admin_profil()
	if request.method == 'POST':
		user_form = CreateUserForm(request.POST)
		profil_form = Create_admin_profil(request.POST)
		if user_form.is_valid() and profil_form.is_valid():
			user = user_form.save()
			profil = profil_form.save()
			group = Group.objects.get(name='admin')
			user.groups.add(group)
			admin_profil.objects.filter(id=profil.id).update(admin_person=user)
			username = user_form.cleaned_data.get('username')
			messages.success(request, 'Un compte a été créé pour ' + username)
			return redirect ('Connexion_admin')
	context = {'user_form':user_form, 'profil_form':profil_form,}

	return render(request, 'admin_register.html', context)
@unauthenticated_user
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('administrateur_homes')
		else:
			messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
	context = {}
	return render(request, 'login-admin.html', context)

def logoutUser(request):
	logout(request)
	return redirect('Connexion_admin')
#revoir les redirect
@login_required(login_url='Connexion_admin')
@allowed_users(allowed_roles=['admin'])
def admin_home_view(request):
	parking_user = smartParking.objects.all().filter(administ=request.user)
	print (parking_user)
	return render(request,'admin_home.html',{"parkings":parking_user})

@login_required(login_url='Connexion_admin')
@allowed_users(allowed_roles=['admin'])
def admin_parking_create(request):
	admin=admin_profil.objects.get(admin_person=request.user)
	admin_id=admin
	print(admin_id)
	if request.method =="POST":
		compagnie = request.POST.get("compagnie")
		site = request.POST.get("site")
		new_compagnie_site = compagnie+'-'+site
		admin = request.user
		npt=request.POST.get('nombrePlaceTotal')
		time_r=request.POST.get('timeReservation')
		latitude=request.POST.get('latitude')
		longitude=request.POST.get('longitude')
		n_distance=request.POST.get('distance')
		print(new_compagnie_site) 
		id_parkig=smartParking.objects.create(compagnie_site=new_compagnie_site,
									numPlaces=npt,
									reserveDuration=timedelta(minutes=int(time_r)),
									parking_latitude=latitude,
									parking_longitude=longitude,
									distance=n_distance,
									administ=request.user,
									)
		obj=smartParking.objects.get(compagnie_site=new_compagnie_site)
		n_place_user = obj.numPlaces
		for i in range(1, n_place_user+1):
			State.objects.create(placeName=str(i), statePlace=False, parking=id_parkig, place_given_name="")
		return redirect('administrateur_homes')

	context = {}
	return render(request, 'admin.html', context)

@login_required(login_url='Connexion_admin')
@allowed_users(allowed_roles=['admin'])	
def admin_profil_update(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfilUpdate(request.POST,instance= request.user.admin_profil)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,'Votre profil a été modifié')
			return redirect('profil_admin')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfilUpdate(instance=request.user.admin_profil)
	context = {
	'u_form': u_form,
	'p_form': p_form,
	}
	return render(request,'admin_update.html', context)
@login_required(login_url='Connexion_admin')
@allowed_users(allowed_roles=['admin'])
def admin_parking_update(request,id):
	parking = smartParking.objects.get(id=id, administ=request.user)
	places = State.objects.filter(parking=str(parking.id))
	len_p = len(places)
	park= smartParking.objects.filter(id=id, administ=request.user).update(numPlaces=len_p)
	print(parking.numPlaces)
	if request.method == 'POST':
		latitude=request.POST.get('latitude')
		longitude=request.POST.get('longitude')
		d = request.POST.get('distance')
		time_r=request.POST.get('timeReservation')
		places_names = request.POST.getlist('places')
		sup = request.POST.get('sup')
		place_ajouter = request.POST.get('place_ajouter')
		
		smartParking.objects.filter(id=id).update(
			reserveDuration=timedelta(minutes=int(time_r)),
			parking_latitude=latitude,
			parking_longitude=longitude,
			distance=d,
			)
		print(parking.numPlaces)
		if place_ajouter:
			print(place_ajouter)
			last_place = State.objects.filter(parking=str(parking.id)).last()
			n = int(last_place.placeName)
			print(n)
			if place_ajouter == 1:
				State.objects.create(parking=parking,placeName=n+1,statePlace= False, place_given_name='',)
			else:	
				for i in range(n, n+int(place_ajouter)):
					State.objects.create(
					parking=parking,
					placeName=i+1,
					statePlace= False,
					place_given_name='',
					)
					
		if sup:
			State.objects.filter(parking=str(parking.id), placeName=sup).delete()


		for i in range(len(places)):
			places = State.objects.filter(parking=str(parking.id),placeName=(i+1)).update(place_given_name=places_names[i])
			# print(places_names[i])
		places = State.objects.filter(parking=str(parking.id))
		len_p = len(places)
		parking = smartParking.objects.get(id=id, administ=request.user)
		park= smartParking.objects.filter(id=id, administ=request.user).update(numPlaces=len_p)
		print(parking.numPlaces)
		return HttpResponseRedirect(request.path_info)

	context = {
	'parking':parking,
	'places':places,
	'len_p':len_p,
	}
	return render(request, 'parking_update.html',context)

@login_required(login_url='Connexion_admin')
@allowed_users(allowed_roles=['admin'])
def parking_delete(request):
	parkings = smartParking.objects.all().filter(administ=request.user)
	if request.method == 'POST':
		sup = request.POST.get('sup')
		print(sup)
		smartParking.objects.filter(administ=request.user,compagnie_site=sup).delete()
		

	context = {
		'parkings': parkings
	}
	return render(request,'parking_delete.html',context)
def dashbord(request):
	parking = smartParking.objects.all().filter(administ=request.user)
	usr=[]
	ins =[]
	rec=[]
	for park in parking:
		places = State. objects.filter(parking=park)
		# parking= smartParking.objects.filter(id= park.id).update(numPlaces=int(len(places)))
		print(park.numPlaces)
		ins=Reclamation.objects.all().filter(parking=park)
		print(ins)
		# usr.appand(str())
	# rec=Reclamation.objects.all().filter(user=)
	print(ins)
	for i in ins:
		usr=i.user

	n_park= len(parking)

	context = {
	'parking': parking,
	'n_park' : n_park,
	'recs' : ins,
	}
	return render(request, 'dashbord.html',context)
def parking_details(request, id):
	parking=smartParking.objects.get(id=id)
	places=State.objects.all().filter(parking=parking)
	print(places)
	context = {
	'parking': parking,
	'places': places,
	}
	return render(request,'parking_details.html',context)