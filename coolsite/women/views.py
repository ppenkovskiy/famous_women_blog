from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect

def index(request):
    return HttpResponse('Page of "women" application')

def categories(request, category_id):
    return HttpResponse(f'<h1>Categories page</h1><p>{category_id}</p>')

def archive(request, year):
    if int(year) > 2021 :
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archive by year</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found.</h1><h1>Please, try again.</h1>')