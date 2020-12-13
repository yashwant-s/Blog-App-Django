from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
      email = forms.EmailField()

      class Meta:
            model = User #here we saying that when we create a form we will save it to mdel 'User'
            fields = ['username', 'email', 'password1', 'password2'] # this is the order in which we want our field to be displayed in the form


class UserUpdateForm(forms.ModelForm):
      email = forms.EmailField()

      class Meta:
            model = User #here we saying that when we create a form we will save it to mdel 'User'
            fields = ['username', 'email'] # this is the order in which we want our field to be displayed in the form

class ProfileUpdateForm(forms.ModelForm):
      class Meta:
            model = Profile
            fields = ['image']