from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Это страница моего блога! Добро пожаловать!")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям.</h1>")