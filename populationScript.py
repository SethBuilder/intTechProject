import django
from mainapp import models

django.setup()

def populate():

    cities = [{'name': 'Glasgow', 'country': 'Scotland'}, {'name': 'London', 'country': 'England'},
              {'name': 'Stockholm', 'country': 'Sweden'}, {'name': 'Sao Paulo', 'country': 'Brazil'}]
    users = [{'name': 'Bob', 'city': cities[0]}, {'name': 'Arnold', 'city': cities[3]},
             {'name': 'Jacqueline', 'city': cities[2]}, {'name': 'Mary', 'city': cities[1]}]


if __name__ == '__main__':
    populate()
