from django.db import models


# this is the model for city
class City(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)


# this is model for user
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    profilepic = models.ImageField()
    firstname = models.CharField(max_length=128)
    secondname = models.CharField(max_length=128)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.username


# this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
    user = models.ForeignKey(User)
    hobby = models.TextField(max_length=128)

    def __unicode__(self):
        return self.hobby


# this is the model for hobbies - one to many relationship with User
class Language(models.Model):
    user = models.ForeignKey(User)
    language = models.TextField(max_length=128)

    def __unicode__(self):
        return self.language


# this is the model for hobbies - one to many relationship with User
class UserRating(models.Model):
    user = models.ForeignKey(User)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.rating
