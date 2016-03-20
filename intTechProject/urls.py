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

from django.views.generic import RedirectView

from django_messages.views import *


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

    url(r'^messages/', include('django_messages.urls')),

    url(r'^updateprofile/', views.updateprofile, name="updateprofile"),

     url(r'^$', RedirectView.as_view(url='inbox/'), name='messages_redirect'),
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', view, name='messages_detail'),
    url(r'^delete/(?P<message_id>[\d]+)/$', delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),

    url(r'^search/$', views.search, name="search"), ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


