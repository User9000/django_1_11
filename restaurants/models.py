from django.db import models
from django.db.models.signals import pre_save 
from .utils import unique_slug_generator
from  .validators import validate_category

# Create your models here.
class RestaurantLocation(models.Model):
    name       =  models.CharField(max_length=120)
    location   =  models.CharField(max_length=120,null=True, blank=True)
    category   =  models.CharField(max_length=120,null=True, blank=False, validators =[validate_category])
    timestamp  =  models.DateTimeField(auto_now=True)
    updated    =  models.DateTimeField(auto_now=True)
    slug       =  models.SlugField(null=True, blank=True)
    #my_date_field = models.DateField(auto_now=False, auto_now_add=False)

    ##__str__ is the string representation of an object
    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


### Signals handlers
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    print('saving....')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

'''
def rl_post_save_receiver(sender, instance, *args, **kwargs):
    print('saved')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()
    '''

pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)

#post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)