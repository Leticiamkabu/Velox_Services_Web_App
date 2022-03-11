from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class UserSignUp(UserCreationForm):
    first_name  = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name', 'class':'form-control'}))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your last name', 'class':'form-control'}))

    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter a username', 'class':'form-control'}))

    password1 = forms.CharField(max_length=200, label = 'Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password', 'class':'form-control'}))

    password2 = forms.CharField(max_length=200, label = 'Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password', 'class':'form-control'}))
        
    email = forms.EmailField( widget= forms.EmailInput(
        attrs={'placeholder': 'Enter your email', 'class':'form-control'}))
    
    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',)




class UserRegForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control','placeholder':'Username'}
    ), required = True, max_length = 50)

    email = forms.CharField(widget = forms.EmailInput(
        attrs = {'class':'form-control','placeholder':'Email'}
    ), required = True, max_length = 50)

    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {'class':'form-control','placeholder':'Password'}
    ), required = True, max_length = 50)

    password2 = forms.CharField(widget = forms.PasswordInput(
        attrs = {'class':'form-control','placeholder':'Password'}
    ), required = True, max_length = 50)

    class Meta():
        model = User
        fields = ['username','email','password','password2']


class ServiceProviderRegForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control','placeholder':'Username'}
    ), required = True, max_length = 50)

    email = forms.CharField(widget = forms.EmailInput(
        attrs = {'class':'form-control','placeholder':'Email'}
    ), required = True, max_length = 50)

    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {'class':'form-control','placeholder':'Password'}
    ), required = True, max_length = 50)

    # password2 = forms.CharField(widget = forms.PasswordInput(
    #     attrs = {'class':'form-control','placeholder':'Password'}
    # ), required = True, max_length = 50)

    # password = forms.CharField(widget = forms.PasswordInput(
    #     attrs = {'class':'form-control','placeholder':'Password'}
    # ), required = True, max_length = 50)

    class Meta():
        model = User
        fields = ['username','email','password']

