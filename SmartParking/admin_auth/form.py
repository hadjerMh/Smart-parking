from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import admin_profil
class CreateUserForm(UserCreationForm):
	class Meta:
		model =  User
		fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
class Create_admin_profil(forms.ModelForm):
	class Meta:
		model = admin_profil
		fields = ['phone', 'entreprise', 'adress_entreprise']
class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['last_name', 'first_name', 'email']
class ProfilUpdate(forms.ModelForm):
	class Meta:
		model = admin_profil
		fields = ['phone', 'adress_entreprise']
		