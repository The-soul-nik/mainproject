from django.urls import path
from .import views
from django.conf.urls import url

app_name = 'arts'

urlpatterns = [
    path('', views.home, name='home'),
    url('rocket', views.minimale),
    url(r'^(?P<slug>[\w-]+)/landscapes$', views.detailus, name='detailus'), 
    url(r'^(?P<slug>[\w-]+)/minimalism$', views.details, name='details' ),
    url('abstraction', views.abstraction),
    url(r'^abs(?P<slug>[\w-]+)/$', views.detailsabs, name='detailsabs'),
    url('landscapes', views.landscapes, name="landscapes"),

    path('offer', views.offer, name='offer'),
]
