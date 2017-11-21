from django.conf.urls import url

from restaurants.views import ResturantCreateView,  RestaurantListView, RestaurantDetailView


##################################################################
urlpatterns = [

    url(r'$', RestaurantListView.as_view(),name='list'),
    url(r'^create/$',ResturantCreateView.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
        
 ]
