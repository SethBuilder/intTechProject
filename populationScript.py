import os
import json
import urllib2
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intTechProject.settings')

django.setup()

from django.contrib.auth.models import User
from mainapp.models import City, Hobby, UserProfile, Language, UserRating


def create_users():
    cities = ['Glasgow', 'Madrid', 'Stockholm', 'Sao Paulo', 'Shanghai', 'Paris', 'Munich', 'Budapest']
    countries = ['Scotland', 'Spain', 'Sweden', 'Brazil', 'China', 'France', 'Germany', 'Hungary']

    languages = ['English', 'Spanish', 'Swedish', 'Portuguese', 'Chinese', 'French', 'German', 'Hungarian', 'Latin',
                 'Japanese', 'Thai']

    email_suffixes = ['live.com', 'live.co.uk', 'hotmail.com', 'gmail.com', 'yahoo.com', 'apple.com', 'aol.com']

    # Read in names from file
    names_file = open("static/populationScriptFiles/newNamesMale.txt", 'r')
    male_names = names_file.readlines()

    names_file = open("static/populationScriptFiles/namesFemale.txt", 'r')
    female_names = names_file.readlines()

    names_file = open("static/populationScriptFiles/namesLast.txt", 'r')
    last_names = names_file.readlines()

    city_descriptions_file = open("static/populationScriptFiles/cityDescriptions.txt", 'r')
    city_descriptions = city_descriptions_file.readlines()

    # Read in popular hobbies from file
    hobbies_file = open("static/populationScriptFiles/hobbies.txt", 'r')
    hobby_names = hobbies_file.readlines()

    # new_names_file = open("populationScriptFiles/namesFemale.txt", 'w')

    # for name in names:
    # name = re.split(' ', name)
    # cnew_names_file.write(name[0] + '\n')

    for new_person in range(0, 100):

        # Create a male profile if random number is 1 (50% chance), female profile otherwise
        if random.randint(0, 1) == 1:
            gender = 'male'
            first_name = male_names[random.randint(0, len(male_names) - 1)].strip().title()

        else:
            gender = 'female'
            first_name = female_names[random.randint(0, len(female_names) - 1)].strip().title()

        # Assign user a random surname
        last_name = last_names[random.randint(0, len(last_names) - 1)].strip().title()

        # Create an email address in the form <first name>.<surname>@<random email suffix>
        email_suffix = email_suffixes[random.randint(0, len(email_suffixes) - 1)].strip()
        email = first_name.lower() + '.' + last_name.lower() + '@' + email_suffix

        # Create a username
        username = first_name.lower() + last_name.lower()

        # Set all passwords to be passwords for testing (could be changed later)
        password = 'password'

        # Assign user a random city
        random_city = random.randint(0, len(cities) - 1)
        city = cities[random_city]
        country = countries[random_city]
        description = city_descriptions[random_city]

        profile_picture = open("static/populationScriptFiles/Images/maleProfile1.jpg", 'r')

        created_city = City.objects.get_or_create(name=city, country=country, description=description)[0]
        created_city.country = country
        created_city.save()

        new_user = User.objects.get_or_create(username=username, email=email)[0]
        #new_user.profilepic = profile_picture
        new_user.first_name = first_name
        new_user.last_name = last_name

        new_user.save()

        new_user_profile = UserProfile.objects.get_or_create(user=new_user, city=created_city, )[0]
        new_user_profile.slug = username
        new_user_profile.save()

        # Assign user a random number of hobbies between 0 and 5 (up to a total of six hobbies)
        user_hobbies = []
        for new_hobby in range(random.randint(0, 6)):
            hob = hobby_names[random.randint(0, len(hobby_names) - 1)].strip().title()
            if hob not in user_hobbies:
                user_hobbies.append(hob)
                new_hobby = Hobby.objects.get_or_create(hobby=hob)[0]
                new_hobby.save()
                new_user_profile.hobbies.add(new_hobby)

        # Assign user the language native to that city (e.g. Glasgow would be English)
        # The arrays are in the correct order so the city at index 0 will correspond to the language at index 0
        new_language = Language.objects.get_or_create(language=languages[random_city])[0]
        new_language.save()
        new_user_profile.languages.add(new_language)
        user_languages = [languages[random_city]]

        # Assign user a random number of other languages between 0 and 3 (up to a total of four languages)
        for new_language in range(random.randint(0, 3)):
            lang = languages[random.randint(0, len(languages) - 1)]
            if lang not in user_languages:
                new_language = Language.objects.get_or_create(language=lang)[0]
                new_language.save()
                new_user_profile.languages.add(new_language)
                user_languages.append(lang)

        # Save the new user
        new_user_profile.save()


def leave_reviews():

    # Read in random reviews from file
    reviews_file = open("static/populationScriptFiles/reviews.txt", 'r')
    reviews = reviews_file.readlines()

    users = UserProfile.objects.all()
    for new_reviewer in users:

        # Put new_reviewer in users_reviewed so they never review themselves
        users_reviewed = [new_reviewer]

        for new_review in range(random.randint(1, 5)):

            new_rev = reviews[random.randint(0, len(reviews) - 1)].strip()
            new_rev = new_rev.split(', ', 2)
            rev = new_rev[0]
            rating = new_rev[1]

            reviewee = users[random.randint(0, len(users) - 1)]

            if reviewee not in users_reviewed:
                rev = UserRating.objects.get_or_create(user=reviewee, rating_user=new_reviewer, comment=rev,
                                                       rating=int(rating))[0]
                # rev.save()
                users_reviewed.append(reviewee)


if __name__ == '__main__':
    create_users()
    leave_reviews()
