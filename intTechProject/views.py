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
    
"""
def signup(request):

    # Set to False initially. Code changes value to True when signup succeeds.
    signedup = False

    # When it is a HTTP POST, we process it form data.
    if request.method == 'POST':

        # It grabs the information from the form information
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        #If both forms are valid, save the data to the database.

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()


            # set up the password and save it.

            user.set_password(user.password)
            user.save()

            # sorting the UserProfile instance
            profile = profile_form.save(commit=False)
            profile.user = user

            #If the user has provided the picture, get it from the form and save it in the UserProfile and save it.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            # inform the template that the signup was successful.
            signedup = True

            # If not successful show the problem to the user as well as on the terminal

        else:
            print user_form.errors, profile_form.errors

    #if not an HTTP POST , form will be rendered using two ModelForm instances and the forms will be blank for
    # user input.

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request, 'signup.html')


def login(request):


    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

    #'user_form': user_form, 'profile_form': profile_form, 'signedup': signedup
     """
