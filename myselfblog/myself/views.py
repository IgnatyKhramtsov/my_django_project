from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify, first

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

class MyClass:
     def __init__(self, a, b):
         self.a = a
         self.b = b

def index(request):
    # t = render_to_string('myself/index.html')
    # return HttpResponse(t)
    # return HttpResponse("Это страница моего блога! Добро пожаловать!")
    data = {
        'title': 'Главная страница',
        'main_title': 'My Blog',
        'menu': menu,
        'float': 28.65,
        'lst': [1, 2, 'dsd', True],
        'set': {1, 1, 2, 5},
        'dict': {'k1': 'v1', 'k2': 'v2'},
        'obj': MyClass(10, 20),
        'url': slugify('The Main')
    }
    return render(request, 'myself/index.html', context=data)


def about(request):
    return render(request, 'myself/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(cat_slug)
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return redirect(uri)
        # return redirect('cats', 'music') <-- Или можно так kod: 302, if permanent=True kod: 301
        # rerutn HttpResponsePermanentRedirect(uri) <-- kod: 301
        # rerutn HttpResponseRedirect(uri) <-- kod: 302
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


