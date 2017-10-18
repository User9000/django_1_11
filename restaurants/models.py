from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name       =  models.CharField(max_length=120)
    location   =  models.CharField(max_length=120,null=True, blank=True)
    category   =  models.CharField(max_length=120,null=True, blank=False)
    timestamp  =  models.DateTimeField(auto_now=True)
    updated    =  models.DateTimeField(auto_now=True)
    #my_date_field = models.DateField(auto_now=False, auto_now_add=False)

    ##__str__ is the string representation of an object
    def __str__(self):
        return self.name


