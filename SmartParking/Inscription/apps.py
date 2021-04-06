from django.apps import AppConfig


class InscriptionConfig(AppConfig):
    name = 'Inscription'
    def ready(self):
    	import Inscription.signals