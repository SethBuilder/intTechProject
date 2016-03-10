from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# this is the model for city
class City(models.Model):
    # May have to change unique=true here
    name = models.CharField(max_length=128, default="", unique=True)
    country = models.CharField(max_length=128, default="Scotland")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


# this is model for user
class UserProfile(models.Model):
    user = models.OneToOneField(User)
#username = models.CharField(max_length=128, unique=True)
    
#email = models.EmailField(max_length=128, unique=True)
    # password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    profilepic = models.ImageField(blank=True)
    
#firstname = models.CharField(max_length=128, null=True)
    
#secondname = models.CharField(max_length=128, null=True)
    city = models.ForeignKey(City)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes

        @property
        def avg_rating(User):
            return userrating = User.userrating_set.all().aggregate(Avg('rating'))['rating__avg']


# this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
    users = models.ManyToManyField(User)
    hobby = models.CharField(max_length=128)

    def __unicode__(self):
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username

        return self.hobby


# this is the model for languages - one to many relationship with User
class Language(models.Model):
    users = models.ManyToManyField(User)
    language = models.CharField(max_length=128)

    def __unicode__(self):
        return self.language


# this is the model for user ratings - one to many relationship with User
class UserRating(models.Model):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=500)
    for_username = models.CharField(max_length=128)
    rating = models.IntegerField(default=5)

    def __unicode__(self):
        return unicode(self.rating)



