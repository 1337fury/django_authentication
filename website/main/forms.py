from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegistrationForm(UserCreationForm): # UserCreationForm is a form that is provided by Django that is used for creating new users
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["username"].widget.attrs.update({
			"autofocus": True
		})

class PostForm(forms.ModelForm): # forms.ModelForm is a class that inherits from forms.Form and is used for creating forms that interact with models
	class Meta:
		model = Post
		fields = ["title", "content"]
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["title"].widget.attrs.update({
			"autofocus": True
		})