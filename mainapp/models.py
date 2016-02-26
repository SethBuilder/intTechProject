from django.db import models
from django.db.models import Avg


#this is the model for city
class City(models.Model):
	name = models.CharField(max_length=128, default="")
	country = models.CharField(max_length=128, default="Scotland")

	def __unicode__(self):
		return self.name



# this is the model for city
class City(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)


# this is model for user
class User(models.Model):
<<<<<<< HEAD
	username = models.CharField(max_length=128, unique=True)
	email = models.EmailField(max_length=128, unique=True)
	#password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	profilepic = models.ImageField(null=True)
	firstname = models.CharField(max_length=128, null=True)
	secondname = models.CharField(max_length=128, null=True)
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.username
	@property
	def avg_rating(self):
			return self.userrating_set.all().aggregate(Avg('rating'))['rating__avg']

#this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
	user = models.ForeignKey(User)
	hobby = models.CharField(max_length=128)
||||||| merged common ancestors
	username = models.CharField(max_length=128, unique=True)
	email = models.EmailField(max_length=128, unique=True)
	#password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	profilepic = models.ImageField()
	firstname = models.CharField(max_length=128)
	secondname = models.CharField(max_length=128)
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.username

#this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
	user = models.ForeignKey(User)
	hobby = models.TextField(max_length=128)
=======
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    profilepic = models.ImageField()
    firstname = models.CharField(max_length=128)
    secondname = models.CharField(max_length=128)
    city = models.ForeignKey(City)
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8

    def __unicode__(self):
        return self.username


<<<<<<< HEAD
#this is the model for languages - one to many relationship with User
class Language(models.Model):
	user = models.ForeignKey(User)
	language = models.CharField(max_length=128)
||||||| merged common ancestors
#this is the model for hobbies - one to many relationship with User
class Language(models.Model):
	user = models.ForeignKey(User)
	language = models.TextField(max_length=128)
=======
# this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
    user = models.ForeignKey(User)
    hobby = models.TextField(max_length=128)
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8

    def __unicode__(self):
        return self.hobby

<<<<<<< HEAD
#this is the model for user ratings - one to many relationship with User
class UserRating(models.Model):
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=500)
	for_username = models.CharField(max_length=128)
	rating = models.IntegerField(default=5)
||||||| merged common ancestors
#this is the model for hobbies - one to many relationship with User
class UserRating(models.Model):
	user = models.ForeignKey(User)
	comment = models.TextField(max_length=500)
	rating = models.IntegerField(default=0)
=======
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8

<<<<<<< HEAD
	def __unicode__(self):
		return unicode(self.rating)
||||||| merged common ancestors
	def __unicode__(self):
		return self.rating
=======
# this is the model for hobbies - one to many relationship with User
class Language(models.Model):
    user = models.ForeignKey(User)
    language = models.TextField(max_length=128)
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8

<<<<<<< HEAD
||||||| merged common ancestors
#this is the model for city
class City(models.Model):
	name = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
=======
    def __unicode__(self):
        return self.language
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8


# this is the model for hobbies - one to many relationship with User
class UserRating(models.Model):
    user = models.ForeignKey(User)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.rating
