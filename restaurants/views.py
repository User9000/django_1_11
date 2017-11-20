

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm



##function based view
@login_required(login_url='/login/')
def restaurant_createview(request):
        form = RestaurantLocationCreateForm(request.POST or None)
        errors = None
        if form.is_valid():
            if request.user.is_authenticated():
                instance = form.save(commit=False)
                instance.owner = request.user
                instance.save()
                #form.save()
                return HttpResponseRedirect("/restaurants/")
            else:
                return HttpResponseRedirect("/login/")
        if form.errors:
               errors = form.errors
        template_name = 'restaurants/forms.html'
        context = { "form": form, "error": errors }
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
            #print("we did it")
        else:
            queryset = RestaurantLocation.objects.all()
            #print("we did not")

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


class ResturantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "form.html"
    login_url = "/login/"

    def form_valid(self, form):
         instance = form.save(commit=False)
         instance.owner = self.request.user
         #instance.save()
         return super(ResturantCreateView, self).form_valid(form)


    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant '
        return context