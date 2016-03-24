from django.db import models
from django.db.models import Avg
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# this is the model for city
class City(models.Model):
    # May have to change unique=true here
    name = models.CharField(max_length=128, default="", unique=True)
    country = models.CharField(max_length=128, default="Scotland")
    information = models.CharField(max_length=3000, default="")
    image = models.ImageField(upload_to='city_images', default=0)
    slug = models.SlugField(unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


# this is the model for hobbies - one to many relationship with User
class Hobby(models.Model):
    hobby = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.hobby)
        super(Hobby, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.hobby


# this is the model for languages - one to many relationship with User
class Language(models.Model):
    language = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # if self.id is None:
        # self.slug = slugify(self.name)
        self.slug = slugify(self.language)
        super(Language, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.language


# this is model for user
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    hobbies = models.ManyToManyField(Hobby)
    languages = models.ManyToManyField(Language)

    profilepic = models.ImageField(upload_to='profile_pictures', blank=False)
    city = models.ForeignKey(City)
    slug = models.SlugField(unique=True)

    average_rating = models.IntegerField(default=0)
    ratings_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        # Uncomment if you don't want the slug to change every time the name changes
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username

    def update_average_rating(self, new_rating, *args, **kwargs):

        old_total = self.average_rating * self.ratings_count

        self.ratings_count += 1

        # Find new average
        self.average_rating = (old_total + new_rating) / self.ratings_count
        print self.user.first_name + str(self.average_rating)
        super(UserProfile, self).save(*args, **kwargs)

    def get_range_average(self):
        print self.average_rating
        return range(self.average_rating)


# this is the model for user ratings - one to many relationship with User
class UserRating(models.Model):
    user = models.ForeignKey(UserProfile, related_name="rated_user")
    rating_user = models.ForeignKey(UserProfile, related_name="rating_user")
    comment = models.CharField(max_length=500, blank=True)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)
        ])

    def save(self, *args, **kwargs):
        self.user.update_average_rating(self.rating)
        super(UserRating, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.rating)

    def get_range(self):
        return range(self.rating)



