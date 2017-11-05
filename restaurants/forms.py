from django import forms
from .models import RestaurantLocation

class RestaurantCreateForm(forms.Form):

    name       =  forms.CharField()
    location   =  forms.CharField(required = False)
    category   =  forms.CharField(required = False)

#### clean_<FIELD> the clean is used to validate the data.
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name


class RestaurantLocationCreateForm(forms.ModelForm):
        class Meta:
            model = RestaurantLocation
            fields = [
                'name',
                'location',
                'category'
            ]

