from django.shortcuts import render
from .models import Games, Films
import random



def offers(request):
    return render(request, 'where/offers.html')

def game(request):
    gamesss = Games.objects.count()
    gamess = Games.objects.all()
    random_gamess = random.sample(list(gamess), gamesss)
    return render(request, 'where/game.html', {'random_gamess':random_gamess})


def detailgame(request, slug):
    games = Games.objects.get(slug=slug)
    return render(request, 'where/gamedet.html', {'games':games})


def film(request):
    filmsss = Films.objects.count()
    filmss = Films.objects.all()
    random_gamess = random.sample(list(filmss), filmsss)
    return render(request, 'where/film.html', {'random_gamess':random_gamess})


def detailfilms(request, slug2):
    films = Films.objects.get(slug=slug2)
    return render(request, 'where/filmdet.html', {'films':films})
