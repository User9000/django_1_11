from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import random

#FBV Function Based Views
def home(request):
    num = random.randint(0,100000)
    some_list = [num, random.randint(0,100000),random.randint(0,100000)]
    context = {
        "bool_item":False,
        "num": num,
        "some_list":some_list
    }
    return render(request, "base.html", context) #response


