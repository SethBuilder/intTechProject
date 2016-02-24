from django.shortcuts import render
from mainapp.models import User

def base_profile(request):
    return render(request, 'base.html')


def index(request):
	user_list = User.objects.all()
	context_dict = {"users" : user_list}

	return render(request, "index.html", context_dict)

