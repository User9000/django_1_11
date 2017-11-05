

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm


def restaurant_createview(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        category = request.POST.get("category")
        obj  = RestaurantLocation.objects.create(
                name=title, 
                location = location, 
                category = category
                )
        return HttpResponseRedirect('/restaurants/')

    template_name = 'restaurants/forms.html'

    context = {}
    return render(request,template_name, context)
# Create your views here.
def restaurant_listview(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request,template_name, context)


class RestaurantListView(ListView):
   
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(Q(category__iexact = slug) | Q(category__icontains = slug))
            print("we did it")
        else:
            queryset = RestaurantLocation.objects.all()
            print("we did not")

        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()    


def restaurant_detailview(request, slug):
    template_name = 'restaurant/restauranlocation_detail.html'
    obj = RestaurantLocation.objects(slug=slug)
    context = {
        "object": obj,
    }
    return render(request, template_name, context)