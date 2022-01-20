from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

menu = [{'title': "About page", "url_name": "about"},
        {'title': "Add a blog", "url_name": "add_page"},
        {'title': "Feedback", "url_name": "contact"},
        {'title': "Login", "url_name": "login"},
        ]

def index(request):
    posts = Women.objects.all()

    context = {
               'posts': posts,
               'menu': menu,
               'title': 'Home page',
               'cat_selected': 0
    }

    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About page'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found.</h1><h1>Please, try again.</h1>')

def addpage(request):
    return HttpResponseNotFound('Add page')

def contact(request):
    return HttpResponseNotFound('Contact us')

def login(request):
    return HttpResponseNotFound('Login')

def show_post(request, post_id):
    return HttpResponse(f"Post with id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
               'posts': posts,
               'menu': menu,
               'title': 'Categories',
               'cat_selected': 0
    }

    return render(request, 'women/index.html', context=context)