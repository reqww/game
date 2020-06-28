from django import forms
from django.contrib.auth.models import User 
from accounts.models import Profile

class RegistrationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
	username = forms.CharField(label='Username')
	first_name = forms.CharField(label='Your name')
	email = forms.CharField(label='Email')


	class Meta:
		model = User
		fields = ("username", "first_name", "email")

	def clean_password2(self):
		cd = self.cleaned_data
		if cd["password"] != cd["password2"]:
			raise forms.ValidationError("Пароли не совпадают")
		else:
			if len(cd["password"])<8:
				raise forms.ValidationError("Слишком короткий пароль")
			else:
				return cd["password2"]

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("username", "first_name","email")

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ("avatar",)
