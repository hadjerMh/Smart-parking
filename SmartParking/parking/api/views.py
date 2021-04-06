from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializer import StateSerializer, ReservationSerializer, ReclamationSerialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from parking.models import State, Reservation, Reclamation


@api_view(['GET'])
def places_ipa(request,parking):
	places = State.objects.all().filter(parking=parking)
	serializer = StateSerializer(places, many=True)
	return Response(serializer.data)

@api_view(['GET', 'POST'])
def places_update(request, pk1):
	place=State.objects.get(id=pk1)
	serializer=StateSerializer(instance=place,data=request.data)#
	if serializer.is_valid():
	 	serializer.save()
	return Response(serializer.data)


@api_view(['GET'])	
def reservation_api(request):
	reservation = Reservation.objects.all()
	serializer = ReservationSerializer(reservation,many=True)
	return Response(serializer.data)

@api_view(['GET','POST'])		
def reservation_update_api(request, pk):
	reservation=Reservation.objects.get(id=pk)
	serializer=ReservationSerializer(instance=reservation, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def reservation_detail_api(request,pk):
	reservation=Reservation.objects.get(id=pk)
	serializer=ReservationSerializer(instance=reservation, many=False)
	return Response(serializer.data)
@api_view(['GET'])
def reclamation_api(request,id):
	reclamtion=Reclamation.objects.all().filter(parking=id)
	serializer= ReclamationSerialize(instance=reclamtion, many=True)
	return Response(serializer.data)