import os
import json
import urllib2
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intTechProject.settings')

django.setup()

from mainapp.models import User, City, Hobby

def populate():
    cities = ['Glasgow', 'Madrid', 'Stolkholm', 'Sao Paulo', 'Shanghai', 'Paris', 'Munich', 'Budapest']
    countries = ['Scotland', 'Spain', 'Sweden', 'Brazil', 'China', 'France', 'Germany', 'Hungary']

    languages = ['English', 'Spanish', 'Swedish', 'Portuguese', 'Chinese', 'French', 'German', 'Hungarian', 'Latin',
                 'Japanese', 'Thai']
    hobbies = ['Visiting museums', 'Sports', 'Skiing', 'Snowboarding', 'Jet Skiing', 'Bungee Jumping', 'Reading',
               'Music', 'Live Music', 'Films', 'Board Games', 'Food']
    email_suffixes = ['live.com', 'live.co.uk', 'hotmail.com', 'gmail.com', 'yahoo.com', 'apple.com', 'aol.com']

    # Read in names from file
    names_file = open("static/populationScriptFiles/newNamesMale.txt", 'r')
    male_names = names_file.readlines()

    names_file = open("static/populationScriptFiles/namesFemale.txt", 'r')
    female_names = names_file.readlines()

    names_file = open("static/populationScriptFiles/namesLast.txt", 'r')
    last_names = names_file.readlines()

    # new_names_file = open("populationScriptFiles/namesFemale.txt", 'w')

    # for name in names:
    # name = re.split(' ', name)
    # cnew_names_file.write(name[0] + '\n')

    for new_person in range(0, 5):

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

        # Assign user the language native to that city (e.g. Glasgow would be English)
        # The arrays are in the correct order so the city at index 0 will correspond to the language at index 0
        user_languages = [languages[random_city]]

        # Assign user a random number of other languages between 0 and 3 (up to a total of four languages)
        for new_language in range(random.randint(0, 3)):
            lang = languages[random.randint(0, len(languages) - 1)]
            if lang not in user_languages:
                user_languages.append(lang)

        # Assign user a random number of hobbies between 0 and 5 (up to a total of six hobbies)
        user_hobbies = []
        for new_hobby in range(random.randint(0, 6)):
            hob = hobbies[random.randint(0, len(hobbies) - 1)]
            if hob not in user_hobbies:
                user_hobbies.append(hob)

        profile_picture = open("static/populationScriptFiles/Images/maleProfile1.jpg", 'r')

        created_city = City.objects.get_or_create(name=city, country=country)[0]
        created_city.country = country
        created_city.save()

        new_user = User.objects.get_or_create(username=username, email=email, city=created_city)[0]
        #new_user.profilepic = profile_picture
        new_user.firstname = first_name
        new_user.secondname = last_name
        new_user.slug = username

        new_user.save()



if __name__ == '__main__':
    populate()
