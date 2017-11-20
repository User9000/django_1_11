

from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    class Mete:
        model = Item
        field =[
            'name',
            'restaurant',
            'contents',
            'excludes',
            'public',
        ]

