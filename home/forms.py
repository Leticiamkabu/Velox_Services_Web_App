from django.forms import ModelForm
from .models import *
from .forms import *
from django import forms

Category =[
        ('LV','Love'),
        ('HV', 'Hate'),
]
class Create_ServiceForm(ModelForm):
    service_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Service name"}))
    description = forms.CharField(max_length = 500, widget = forms.Textarea(attrs = {"class": "form-control", "placeholder": "Service discription"}))
    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs = {"class": "form-control", "placeholder": "Enter Email"}))
    phone_number = forms.CharField( widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Phone number"}))
    image = forms.ImageField(max_length = 100, widget = forms.FileInput(attrs = {"class": "form-control", "placeholder": "Choose image"}))
    category = forms.ChoiceField(choices=Category)
    

    class Meta:
        model = Create_Service
        fields = '__all__'
