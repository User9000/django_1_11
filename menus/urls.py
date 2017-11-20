from django.conf.urls import url

from menus.views import (
    ItemCreateView,
    ItemUpdateView,
    ItemListView,
    ItemDetailView,
)

urlpatterns = [

    url(r'^create/$',ItemCreateView.as_view(),name='create'),
    url(r'^(?P<pk>[\w-]+)/$', ItemDetailView.as_view(), name='detail'),
    url(r'$', ItemListView.as_view(),name='list'),
    
    
 ]