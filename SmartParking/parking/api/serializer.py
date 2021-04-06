from rest_framework import serializers
from parking.models import State, Reservation, Reclamation

class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
			model = Reservation
			fields = ['user', 'R', 'arrived', 'timeout', "number_reservation", "scan_entre", "scan_out"]	
class ReclamationSerialize(serializers.ModelSerializer):
	class Meta:
		model = Reclamation
		fields = '__all__'