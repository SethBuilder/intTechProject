from django.shortcuts import render
# from django.contrib.auth.models import User
from mainapp.models import UserProfile, UserRating, City, Hobby, Language
from django.db.models import Sum
from django.db.models import Avg
from django.db.models import Count
from mainapp.forms import UserForm, UserProfileForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def index(request):
    user_list = UserProfile.objects.select_related().annotate(rating=Avg('rated_user__rating')).order_by('-rating')[:5]
    city_list = City.objects.select_related().annotate(total=Count('userprofile__id')).order_by('-total')[:5]

    #is the logged in with a profile (status = 2) or logged in without a profile (status = 1) or not logged in (status = 0)?
    status = navbatlogic(request=request)

    #to get the profile link in the nav bar (only viewable when logged + has a profile)
    slug_of_logged_user = get_profile_slug(request=request)

    #to get the firstname of the logged in user to customize greeting
    if status==2:
        if not request.user.first_name == None:
            firstname_of_logged_user = request.user.first_name
    else:
        firstname_of_logged_user = None

    context_dict = {"users": user_list, "cities": city_list, "firstname_of_logged_user": firstname_of_logged_user, "slug_of_logged_user": slug_of_logged_user, "status":status}
    

    error = False
    if 'q' in request.GET:
        q = request.GET.get('q')
        if not q:
            error = True
        else:
            try:
                try: 
                    return city(request, q)
                except:
                    cities = City.objects.filter(Q(name__icontains=q) | Q(slug__icontains=q))
                    users = User.objects.filter(Q(username__icontains=q) | Q(profile__slug__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q))
                    
                    searchText = 'Looking for something?'
                    
                    return render(request, 'search_results.html', {'cities': cities, 'users': users, 'query': q, 'searchText': searchText})
            except:
                return render(request, 'search_results.html', {'searchText': searchText})
            
    else:
        if 'city' in request.GET:
            citysearch = request.GET.get('city')
            if not citysearch:
                error = True
            else:
                try:
                    try:
                        return city(request, citysearch)
                    except:
                        cities = City.objects.filter(name__icontains=citysearch)
                        
                        searchText = 'Looking for someplace nice?'
                        
                        return render(request, 'search_results.html', {'cities': cities, 'query': citysearch, 'searchText': searchText, 'cityOnly': 1})
                except:
                    return render(request, 'search_results.html', {'searchText': searchText, 'cityOnly':1})

    return render(request, "index.html", context_dict)


def city(request, city_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    #is the logged in with a profile (status = 2) or logged in without a profile (status = 1) or not logged in (status = 0)?
    status = navbatlogic(request=request)

    #to get the profile link in the nav bar (only viewable when logged + has a profile)
    slug_of_logged_user = get_profile_slug(request=request)

    try:
        # Can we find a city name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        city_name = City.objects.get(slug=city_name_slug)

        # We also add the city object from the database to the context dictionary.
        # We'll use this in the template to verify that the city exists.
        # context_dict['city'] = city

        user_list = User.objects.filter(profile__city=city_name).order_by('-profile__average_rating')[:20]
        hobbies = Hobby.objects.all()
        languages = Language.objects.all()

        context_dict = {"users": user_list, "city": city_name, "all_hobbies": hobbies, "all_languages": languages, "slug_of_logged_user": slug_of_logged_user, "status":status}
        return render(request, 'cityProfile.html', context_dict)

    except city.DoesNotExist:
        # We get here if we didn't find the specified city.
        # Don't do anything - the template displays the "no city" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'city.html', context_dict)


def user(request, user_name_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    #is the logged in with a profile (status = 2) or logged in without a profile (status = 1) or not logged in (status = 0)?
    status = navbatlogic(request=request)

    #to get the profile link in the nav bar (only viewable when logged + has a profile)
    slug_of_logged_user = get_profile_slug(request=request)

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
        context_dict['slug_of_logged_user'] = slug_of_logged_user
        context_dict['status'] = status
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
 

def search(request):

    #is the logged in with a profile (status = 2) or logged in without a profile (status = 1) or not logged in (status = 0)?
    status = navbatlogic(request=request)

    #to get the profile link in the nav bar (only viewable when logged + has a profile)
    slug_of_logged_user = get_profile_slug(request=request)

    error = False
    if 'q' in request.GET:
        q = request.GET.get('q')
        if not q:
            error = True
        else:
            try:
                try: 
                    return city(request, q)
                except:
                    cities = City.objects.filter(Q(name__icontains=q) | Q(slug__icontains=q))
                    users = User.objects.filter(Q(username__icontains=q) | Q(profile__slug__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q))
                    
                    searchText = 'Looking for something?'
                    
                    return render(request, 'search_results.html', {'cities': cities, 'users': users, 'query': q, 'searchText': searchText, "slug_of_logged_user": slug_of_logged_user, "status":status})
            except:
                return render(request, 'search_results.html', {'searchText': searchText, "slug_of_logged_user": slug_of_logged_user, "status":status})
            
    else:
        if 'city' in request.GET:
            citysearch = request.GET.get('city')
            if not citysearch:
                error = True
            else:
                try:
                    try:
                        return city(request, citysearch)
                    except:
                        cities = City.objects.filter(name__icontains=citysearch)
                        
                        searchText = 'Looking for someplace nice?'
                        
                        return render(request, 'search_results.html', {'cities': cities, 'query': citysearch, 'searchText': searchText, 'cityOnly': 1, "slug_of_logged_user": slug_of_logged_user, "status":status})
                except:
                    return render(request, 'search_results.html', {'searchText': searchText, 'cityOnly':1, "slug_of_logged_user": slug_of_logged_user, "status":status})
    
    return render(request, 'search_results.html', {"slug_of_logged_user": slug_of_logged_user, "status":status})


def createprofile(request):
    #is the logged in with a profile (status = 2) or logged in without a profile (status = 1) or not logged in (status = 0)?
    status = navbatlogic(request=request)

    #to get the profile link in the nav bar (only viewable when logged + has a profile)
    slug_of_logged_user = get_profile_slug(request=request)
   
    if request.method == 'POST':
        user = User.objects.get(username = request.user.username)
        user_form = UserForm(data=request.POST, instance = user)

        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profilepic' in request.FILES:
                profile.profilepic = request.FILES['profilepic']
            else:
                profile.profilepic = 'static/images/Profile Pictures/basicUser'

            profile.save()

            profile_form.save_m2m()
           
            if 'next' in request.GET:
                return redirect(request.GET['next'])
        else:
            print user_form.errors, profile_form.errors
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'createprofile.html',
            {'user_form': user_form, 'profile_form': profile_form, "slug_of_logged_user": slug_of_logged_user, "status":status} )

    
def updateprofile(request):
    #is the logged in with a profile (status = 2) or logged in without a profile (status = 1) or not logged in (status = 0)?
    status = navbatlogic(request=request)

    #to get the profile link in the nav bar (only viewable when logged + has a profile)
    slug_of_logged_user = get_profile_slug(request=request)

    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():

            update_user_form.save()
            
            profile = update_profile_form.save(commit=False)

            profile.save()

            update_profile_form.save_m2m()

            return HttpResponseRedirect(reverse('index'))
    else:
        update_user_form = UpdateUserForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)

    #to check if user registered a profile 
    user_has_profile = hasattr(request.user,  'profile')

    if user_has_profile:
            user_profile = getattr(request.user, 'profile')
            user_profile = getattr(user_profile, 'slug')
        
            slug_of_logged_user = user_profile
   
    return render(request, 'updateprofile.html', {'update_user_form' : update_user_form,
     'update_profile_form' : update_profile_form, "slug_of_logged_user": slug_of_logged_user, "status":status})

#status = 0 -->user not logged in
#status = 1 --> user logged in with no profile (just wants to find guides)
#status = 2 --> user logged in with profile (wants to find guides and become a guide as well)
def navbatlogic(request):
    if request.user.is_authenticated():
        if hasattr(request.user,  'profile'):
            status = 2
        else:
            status = 1
    else:
        status = 0
    return status

#to get profile slug of logged user
def get_profile_slug(request):
    status = navbatlogic(request=request)
    if status==2:
        user_profile = getattr(request.user, 'profile')
        user_profile = getattr(user_profile, 'slug')
        slug_of_logged_user = user_profile
    else:
        slug_of_logged_user = None

    return slug_of_logged_user