from django.contrib import admin
from mainapp.models import City, User, Hobby, Language, UserRating


admin.site.register(City)
admin.site.register(User)
admin.site.register(Hobby)
admin.site.register(Language)
admin.site.register(UserRating)

