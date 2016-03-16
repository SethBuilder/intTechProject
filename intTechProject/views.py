from django.shortcuts import render
#from django.contrib.auth.models import User
from mainapp.models import UserProfile
from mainapp.models import UserRating
from mainapp.models import City
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count
from mainapp.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User


def base_profile(request):
    return render(request, 'profilePage.html', {"name": "Blair Calderwood",
                                                "hobbies": ["Drinking", "Stuff", "Climbing", "Not doing uni work",
                                                            "SLIDES"], "languages": ["English", "French", "Spanish",
                                                                                     "Afrikaans"],
                                                "rating_range": range(5)})


def index(request):
    user_list = User.objects.select_related().annotate(rating=Avg('userrating__rating')).order_by('-rating')[:5]

    #to round ratings
   # for user in user_list:
    #    user.rating = int(user.rating)

    # for user in user_list:
        # user.rating_range = range(user.rating)

    city_list = City.objects.select_related().annotate(total=Count('userprofile__id')).order_by('-total')[:5]

    context_dict = {"users": user_list, "cities": city_list, }

    return render(request, "index.html", context_dict)


def city(request, city_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a city name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        city = City.objects.get(slug=city_name_slug)
        
        # We also add the city object from the database to the context dictionary.
        # We'll use this in the template to verify that the city exists.
        #context_dict['city'] = city
        
        user_list = User.objects.filter(profile__city=city)
        context_dict = {"users": user_list, "city": city}
        
    except city.DoesNotExist:
        # We get here if we didn't find the specified city.
        # Don't do anything - the template displays the "no city" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'city.html', context_dict)
    
    
def user(request, user_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a city name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        user = User.objects.select_related('UserProfile').get(profile__slug=user_name_slug)

        context_dict['user_username'] = user.username
        context_dict['user_firstname'] = user.first_name
        context_dict['user_lastname'] = user.last_name

        # We also add the city object from the database to the context dictionary.
        # We'll use this in the template to verify that the city exists.
        context_dict['user'] = user
    except User.DoesNotExist:
        # We get here if we didn't find the specified city.
        # Don't do anything - the template displays the "no city" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'user.html', context_dict)
    
def search(request): 
    return render(request, 'search.html')   
    
def createprofile(request):
    return render(request, 'createprofile.html')
