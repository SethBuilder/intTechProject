from django import forms
from django.contrib.auth.models import User
from mainapp.models import UserProfile, Hobby, Language, City

class UserForm(forms.ModelForm):
      

        class Meta:
            model = User
            fields =  ('first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ('profilepic', 'city')

class HobbyForm(forms.ModelForm):
	class Meta:
		model = Hobby
		fields = ('hobby',)

class LanguageForm(forms.ModelForm):
	class Meta:
		model = Language
		fields = ('language',)