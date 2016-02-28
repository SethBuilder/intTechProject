from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify


#this is the model for city
class City(models.Model):
        name = models.CharField(max_length=128, default="")
        country = models.CharField(max_length=128, default="Scotland")
        slug = models.SlugField()

        def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.name)
            super(City, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.name


#this is model for user
class User(models.Model):
        username = models.CharField(max_length=128, unique=True)
        email = models.EmailField(max_length=128, unique=True)
        #password = forms.CharField(max_length=32, widget=forms.PasswordInput)
        profilepic = models.ImageField(null=True)
        firstname = models.CharField(max_length=128, null=True)
        secondname = models.CharField(max_length=128, null=True)
        city = models.ForeignKey(City)
        slug = models.SlugField()
        
        def save(self, *args, **kwargs):
                # Uncomment if you don't want the slug to change every time the name changes
                #if self.id is None:
                        #self.slug = slugify(self.name)
                self.slug = slugify(self.username)
                super(User, self).save(*args, **kwargs)

        def __unicode__(self):
            return self.username
            
        @property
        def avg_rating(self):
                return self.userrating_set.all().aggregate(Avg('rating'))['rating__avg']

#this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
	user = models.ForeignKey(User)
	hobby = models.CharField(max_length=128)

	def __unicode__(self):
		return self.hobby


#this is the model for languages - one to many relationship with User
class Language(models.Model):
	user = models.ForeignKey(User)
	language = models.CharField(max_length=128)

	def __unicode__(self):
		return self.language

#this is the model for user ratings - one to many relationship with User
class UserRating(models.Model):
	user = models.ForeignKey(User)
	comment = models.CharField(max_length=500)
	for_username = models.CharField(max_length=128)
	rating = models.IntegerField(default=5)

	def __unicode__(self):
		return unicode(self.rating)




