from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_login.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = User
        fields = ('username', 'email',)

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'