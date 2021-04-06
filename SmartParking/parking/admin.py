from django.contrib import admin

# Register your models here.
from .models import smartParking, Reservation, State, Reclamation

admin.site.register(smartParking)
admin.site.register(State)
admin.site.register(Reservation)
admin.site.register(Reclamation)
