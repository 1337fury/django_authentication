from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete=models.CASCADE means that if the user is deleted, all of their posts will be deleted as well
	date_created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the date_created field will be automatically set to the current date and time when a new Post object is created

	def __str__(self):
		return self.title + " | " + str(self.author)
