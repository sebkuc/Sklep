from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    zapytanie = Produkty.objects.all()
    dane = {'kategoria' : kategoria}
    return render(request,'szablon.html')


def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)
