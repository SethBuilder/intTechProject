from django.shortcuts import render
from mainapp.models import User
from mainapp.models import UserRating
from mainapp.models import City
from django.db.models import Sum
from django.db.models import Avg


def base_profile(request):
    return render(request, 'base.html')


def index(request):
	user_list = User.objects.all()
	context_dict = {"users" : user_list}

	return render(request, "index.html", context_dict)

