from django.shortcuts import render


def base_profile(request):
    return render(request, 'base.html')

