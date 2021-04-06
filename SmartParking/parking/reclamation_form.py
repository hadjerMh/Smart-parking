from django.forms import ModelForm
from .models import Reclamation
class Reclamer(ModelForm):
	class Meta:
		model = Reclamation
		fields = ['choice', 'rec_text', 'pic']
	