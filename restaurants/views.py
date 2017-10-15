from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import TemplateView
# Create your views here.
import random


class HomeView(TemplateView):
    template_name="home.html"
    def get_context_data(self, *args,**kwargs):
        num = random.randint(0,100000)
        some_list = [num, random.randint(0,100000),random.randint(0,100000)]
        context = {
            "bool_item":False,
            "num": num,
            "some_list":some_list
        }
        print(context)
        return context

class AboutView(TemplateView):
    template_name="about.html"


class ContactView(TemplateView):
    template_name="contact.html"
