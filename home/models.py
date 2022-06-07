from django.db import models
# from django.forms import ModelForm
# Create your models here.


# class Unique_identification(models.Model):
#     created_date = models.DateTimeField(auto_now_add = True)

#     @classmethod
#     def generate(cls, prefix: str) -> str:
#         instance = cls.objects.create()
#         suffix = f"{instance.pk}".zfill(6)
#         return f"{prefix}-{suffix}"


class Create_Service(models.Model):
    # tracking_id = Unique_identification.generate(prefix = "TI")
    # id = models.CharField(primary_key = True, max_length = 200)
    service_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500) 
    Category =(
        ('Salon','Salon'),
        ('Carpentry', 'Carpentry'),
        ('Tailoring','Tailoring'),
        ('Construction Work','Construction Work'),
    )
    category = models.CharField(max_length = 100, choices = Category )
    email = models.EmailField(max_length = 100)
    phone_number = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    date_updated = models.DateTimeField(auto_now = True, null = True)
    image = models.FileField(upload_to = 'images/',null = True, blank = True)
    # image2 = models.FileField(upload_to = 'images/service_provider',null = True, blank = True)
    
    def __str__(self):
        return self.service_name


class Service_provider(models.Model):
    id = models.CharField(primary_key = True, max_length = 200)
    image2 = models.FileField(upload_to = 'images/service_provider',null = True, blank = True)


    def __str__(self):
        return self.id

