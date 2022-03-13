from django.shortcuts import render, redirect
from .models import smartParking, State, Reservation, Reclamation
from django.contrib.auth.decorators import login_required
from datetime import timedelta
import time
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .reclamation_form import Reclamer
from django.contrib import messages
from Inscription.models import Profil
from Inscription.decoraters import allowed_users


@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def PlacesStatesUser(request):
		#print(obj.placeName)
	try:
		compagnie = Profil.objects.get(user=request.user)
		nom_compagnie = str(compagnie.entreprise)
		print()
		parking_id=smartParking.objects.get(compagnie_site=compagnie.parking.compagnie_site)
		print(parking_id.id)
	
		res=Reservation.objects.get(user=request.user)
		reserve=Reservation.objects.filter(user=request.user).update(scan_out=False)
		print(res.R)
		if res.arrived==False and res.timeout==True:
			place_update = State.objects.filter(user=request.user).update(statePlace=False, user=None)
		#stateid = State.objects.filter(statePlace=False).values_list('id', flat=True)
		if res.R == False:
			if request.method == "POST":
				#b=request.POST.get('y')
				btn=request.POST.get('x')
				print(btn, request.POST)
				changed = State.objects.filter(placeName=btn, parking=parking_id.id).update(statePlace=True, user=request.user)
				rese=Reservation.objects.filter(user=request.user).update(R=True, number_reservation=1)
				
					#changed2=Reservation.objects.filter()
				return redirect ('Reservation');
					#ch=Reservation.objects.filter()
		elif res.arrived == True:
			return redirect ('reservation_success')
		elif res.R == True:
			return redirect('Reservation')
	except Profil.DoesNotExist:
		return HttpResponse("<h1>Le parking n'existe plus</h1>")
	queryset = State.objects.all().filter(parking=parking_id.id)
	np=len(queryset) #nombre de places total
	querysetfalse=State.objects.filter(statePlace=False, parking=parking_id)
	npl=len(querysetfalse)	#nombre de place libre

	context = {
	'object_lists' : queryset,
	'number_places' : np,
	'number_places_free' : npl,
	'res':res,
	'parking_id':parking_id
	}
	return render(request,'home.html',context) 


@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def MakeReservation(request):
	compagnie = Profil.objects.get(user=request.user)
	nom_compagnie = str(compagnie.entreprise)
	parking=smartParking.objects.get(compagnie_site=nom_compagnie)
	longitude = parking.parking_longitude
	latitude = parking.parking_latitude
	distance = parking.distance
	# print(longitude, distance)
	# print(parking)
	delta=Reservation.objects.get(user=request.user)
	if delta.R == True:
		state =  State.objects.get(user=request.user, parking=parking.id)
		print(state)
		r = request.POST.get('home')
		# if r:
		# 	print('r',r)
		if request.method == "POST":
			print('POST')
			delta = Reservation.objects.filter(user=request.user).update(R=False)
			print ('delte',delta)
			state = State.objects.filter(user=request.user,parking=parking.id).update(statePlace=False, user=None)
			return redirect ('home')
		context = {
		'delta': delta,
		'state' : state,
		'parking':parking,
		'long':longitude,
		'lat': latitude,
		'distance': distance,
		}
	else:
		context = {
		'delta': delta,
		}
	if delta.arrived == True:
		return redirect ('reservation_success')
	
		
		# 
		# response.write("<p>Vous n'avez effectué aucune réservation</p>")
		# response.write("<a href={% url 'home'%}>revenir au parking.</p>")
	
	return render(request, 'reservation.html', context)

@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def success_qrcode(request):
	compagnie = Profil.objects.get(user=request.user)
	nom_compagnie = str(compagnie.entreprise)
	parking=smartParking.objects.get(compagnie_site=nom_compagnie)
	state =  State.objects.get(user=request.user, parking=parking.id)
	res = Reservation.objects.get(user=request.user)

	context = {
	'state':state,
	'res': res,
	}
	return render(request,'succes_qrcode.html',context)

@login_required(login_url='Connexion')
@allowed_users(allowed_roles=['customer'])
def reclamations (request):
	ins= Profil.objects.get(user=request.user)
	parking= smartParking.objects.get(compagnie_site=str(ins.entreprise))
	if request.method == "POST":
		form = Reclamer(request.POST, request.FILES)
		if form.is_valid():
			recla = form.save()
			rec=Reclamation.objects.filter(id=recla.id).update(user=request.user, parking=parking)
			messages.success(request,'votre réclamation a été soumise avec succès')
		return redirect('home')	
	else:
		form = Reclamer()
	context = {
	'form' : form,
	}
	return render(request, 'reclamation.html', context)






