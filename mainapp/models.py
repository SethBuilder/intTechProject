from django.db import models

class User(models.Model):
	username = models.CharField(max_length=128, unique=True)
	#email = models.EmailField(max_length=128, unique=True)
	#password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	def __unicode__(self):
		return self.username
