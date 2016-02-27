from django.shortcuts import render
from mainapp.models import User
from mainapp.models import UserRating
from mainapp.models import City
from django.db.models import Sum
from django.db.models import Avg



def base_profile(request):
    return render(request, 'profilePageBase.html')


def index(request):
    user_list = User.objects.all()
    context_dict = {"users": user_list}

    return render(request, "index.html", context_dict)

def city(request, city_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a city name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        city = City.objects.get(slug=city_name_slug)
        context_dict['city_name'] = city.name

        # We also add the city object from the database to the context dictionary.
        # We'll use this in the template to verify that the city exists.
        context_dict['city'] = city
    except city.DoesNotExist:
        # We get here if we didn't find the specified city.
        # Don't do anything - the template displays the "no city" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'city.html', context_dict)