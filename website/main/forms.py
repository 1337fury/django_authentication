from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]
		# labels = {
		# 	"username": "Username",
		# 	"email": "Email",
		# 	"password1": "Password",
		# 	"password2": "Confirm Password"
		# }
		# help_texts = {
		# 	"username": None,
		# 	"email": None,
		# 	"password1": None,
		# 	"password2": None
		# }
		# error_messages = {
		# 	"username": {
		# 		"unique": "This username is already taken."
		# 	}
		# }
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["username"].widget.attrs.update({
			"autofocus": True
		})