from django.contrib import admin
<<<<<<< HEAD
from mainapp.models import User
from mainapp.models import City
from mainapp.models import Hobby
from mainapp.models import Language
from mainapp.models import UserRating
||||||| merged common ancestors
from mainapp.models import User
=======
from mainapp.models import City, User, Hobby, Language, UserRating


admin.site.register(City)
admin.site.register(User)
admin.site.register(Hobby)
admin.site.register(Language)
admin.site.register(UserRating)
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8

<<<<<<< HEAD
admin.site.register(User)
admin.site.register(City)
admin.site.register(Hobby)
admin.site.register(Language)
admin.site.register(UserRating)
||||||| merged common ancestors
admin.site.register(User)
=======
>>>>>>> 3c472991e5bb82df24f74990bf142f06da2ab4c8
