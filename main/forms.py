from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, News


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "email",  "phone_number", "password1", "password2", "profile_picture"]

		
class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title', 'body']



