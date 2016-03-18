"""intTechProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from intTechProject import views
from django.conf.urls import include
from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return "/baseProfile/"

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^city/(?P<city_name_slug>[\w-]+)$', views.city, name='city'),
    url(r'^user/(?P<user_name_slug>\w+)$', views.user, name='user'),
    url(r'^', include('registration.backends.simple.urls')),
    url(r'^createprofile/', views.createprofile, name="createprofile"),
    url(r'^search/$', views.search, name="search"), ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)