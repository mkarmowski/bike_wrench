from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.bike_list, name='bike_list'),
    url(r'^bike/detail/(?P<id>\d+)/$', views.bike_details, name='bike_details'),
    url(r'^bikepart/list/$', views.bikepart_list, name='bikepart_list'),
    url(r'^bikepart/detail/(?P<id>\d+)/$', views.bikepart_details, name='bikepart_details'),
]
