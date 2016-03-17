from django.shortcuts import render
# from django.contrib.auth.models import User
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
from django.db.models import Q


def index(request):
    user_list = UserProfile.objects.select_related().annotate(rating=Avg('rated_user__rating')).order_by('-rating')[:5]

    # to round ratings
    # for user in user_list:
    #    user.rating = int(user.rating)

    city_list = City.objects.select_related().annotate(total=Count('userprofile__id')).order_by('-total')[:5]

    context_dict = {"users": user_list, "cities": city_list,}
    context_dict = {"users": user_list, "cities": city_list, }

    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            try:
                cities = City.objects.filter(name__icontains=q)
                return city(request, q)
            except:
                return render(request, 'search_results.html', {'cities': cities, 'query': q})

    else:
        q2 = request.GET.get('q2')
        if not q2:
            error = True
        else:
            try:
                cities = City.objects.filter(name__icontains=q2)
                users = User.objects.filter(Q(username__icontains=q2) | Q(profile__slug__icontains=q2) | Q(first_name__icontains=q2) | Q(last_name__icontains=q2))
                #return city(request, q)
                return render(request, 'search_results.html', {'cities': cities, 'users': users, 'query': q2})
            except:
                return render(request, 'search_results.html', {'cities': cities, 'users': users, 'query': q2})

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
        # context_dict['city'] = city

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
        user_profile = User.objects.select_related('UserProfile').get(profile__slug=user_name_slug)
        user_profile = UserProfile.objects.get(user=user_profile)
        user_rating = UserRating.objects.filter(user=user_profile)

        context_dict['user'] = user_profile
        context_dict['hobbies'] = user_profile.hobbies.all()
        context_dict['languages'] = user_profile.languages.all()
        context_dict['ratings'] = user_rating
        context_dict['average_ratings'] = user_profile.get_range_average()
        print user_profile.get_range_average()

        # context_dict['user_username'] = user_profile.username
        # context_dict['user_firstname'] = user.first_name
        # context_dict['user_lastname'] = user.last_name

        # We also add the city object from the database to the context dictionary.
        # We'll use this in the template to verify that the city exists.
    except User.DoesNotExist:
        # We get here if we didn't find the specified city.
        # Don't do anything - the template displays the "no city" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'profilePage.html', context_dict)


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            try:
                cities = City.objects.filter(name__icontains=q)
                users = User.objects.filter(Q(username__icontains=q) | Q(profile__slug__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q))
                #return city(request, q)
                return render(request, 'search_results.html', {'cities': cities, 'users': users, 'query': q})
            except:
                return render(request, 'search_results.html', {'cities': cities, 'users': users, 'query': q})

    return render(request, 'search_form.html',
        {'error': error})
    
def createprofile(request):
    return render(request, 'createprofile.html')
