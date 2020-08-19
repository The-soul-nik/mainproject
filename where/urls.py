from django.urls import path
from .import views
from django.conf.urls import url



app_name = 'where'

urlpatterns = [
    path('offers', views.offers, name="offers"),
    url('games', views.game, name="game"),
    url(r'^games(?P<slug>[\w-]+)/$', views.detailgame, name='detailgame' ),
    url('films', views.film, name="film"),
    url(r'^(?P<slug2>[\w-]+)/film$', views.detailfilms, name='detailfilms' ),


]
