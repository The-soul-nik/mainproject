from django.shortcuts import render, redirect
from .models import Minimalism, Abstraction, Landscapes
import random

def offer(request):
    return render(request, 'arts/offer.html')

def home(request):
    return render(request, 'arts/home.html')


def minimale(request):
    minss = Minimalism.objects.count()
    mins = Minimalism.objects.all()
    random_mins = random.sample(list(mins), minss)
    return render(request, 'arts/minimalism.html', {'random_mins':random_mins})


def details(request, slug):

    minimalism = Minimalism.objects.get(slug=slug)
    return render(request, 'arts/details.html', {'minimalism':minimalism})


def detailus(request, slug):
    landscapes = Landscapes.objects.get(slug=slug)
    return render(request, 'arts/landdet.html', {'landscapes':landscapes})


def abstraction(request):
    abstractionss = Abstraction.objects.count()
    abstractions = Abstraction.objects.all()
    random_abstractions = random.sample(list(abstractions), abstractionss)
    return render(request, 'arts/abstraction.html', {'random_abstractions':random_abstractions})


def detailsabs(request, slug):
    abstraction = Abstraction.objects.get(slug=slug)
    return render(request, 'arts/detailabs.html', {'abstraction':abstraction})

def landscapes(request):
    landscapesss = Landscapes.objects.count()
    landscapess = Landscapes.objects.all()
    random_landscapess = random.sample(list(landscapess), landscapesss)
    return render(request, 'arts/landscapes.html', {'random_landscapess':random_landscapess})
