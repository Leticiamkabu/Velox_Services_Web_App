from django.db import models
# from django.forms import ModelForm
# Create your models here.

class Create_Service(models.Model):
    service_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500) 
    Category =(
        ('Love','Lv'),
        ('Hate', 'Ht'),
    )
    category = models.CharField(max_length = 100, choices = Category )
    email = models.EmailField(max_length = 100)
    phone_number = models.IntegerField()
    # date = models.DateTimeField(auto_now_add = True)
    image = models.FileField(upload_to = 'images/',null = True, blank = True)
    
    def __str__(self):
        return self.service_name

