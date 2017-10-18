from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic import TemplateView, ListView
from .models import RestaurantLocation

# Create your views here.
def restaurant_listview(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request,template_name, context)

class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    template_name = "restaurants/restaurants_list.html"

class SearchRestaurantListView(ListView):
    template_name = "restaurants/restaurants_list.html"
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs
        if slug:
            queryset = RestaurantLocation.objects.filter(category__iexact='Mexican' )
        else:
            queryset = RestaurantListView.objects.none()
        return queryset
class AsianRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='Asian Fusion' )
    template_name = "restaurants/restaurants_list.html"

