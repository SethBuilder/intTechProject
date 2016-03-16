from django import forms
from django.contrib.auth.models import User
from mainapp.models import UserProfile, Hobby, Language, City

class UserForm(forms.ModelForm):
        password=forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields =  ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            #fields = ('website', 'picture')
            
            
            
class CityForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the city name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = City
        fields = ('name',)