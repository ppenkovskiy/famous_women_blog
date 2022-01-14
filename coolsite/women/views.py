from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

menu = ['About page', 'Add a blog', 'Feedback', 'Sign In']

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Home page'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About page'})

def categories(request, category_id):
    return HttpResponse(f'<h1>Categories page</h1><p>{category_id}</p>')

def archive(request, year):
    if int(year) > 2021 :
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive by year</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found.</h1><h1>Please, try again.</h1>')