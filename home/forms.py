from django.forms import ModelForm
from .models import *
from .forms import *
from django import forms
from .models import *

Category =[
        ('Salon','Salon'),
        ('Carpentry', 'Carpentry'),
        ('Tailoring','Tailoring'),
        ('Construction Work','Construction Work'),
        ('House Keeping', 'House Keeping'),

]
class Create_ServiceForm(ModelForm):
    id = models.CharField(primary_key = True, max_length = 200)
    service_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Service name"}))
    description = forms.CharField(max_length = 500, widget = forms.Textarea(attrs = {"class": "form-control", "placeholder": "Service discription"}))
    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs = {"class": "form-control", "placeholder": "Enter Email"}))
    phone_number = forms.CharField( widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Phone number"}))
    image = forms.ImageField(max_length = 100, widget = forms.FileInput(attrs = {"class": "form-control", "placeholder": "Choose image"}))
    # image2 = forms.ImageField(max_length = 100, widget = forms.FileInput())
    category = forms.ChoiceField(choices=Category)
    

    class Meta:
        model = Create_Service
        fields = '__all__'


class Service_provider_pic_Form(forms.ModelForm):

    class Meta:
        model = Service_provider
        fields = ['id', 'image2']