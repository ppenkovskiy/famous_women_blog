from django.http import HttpResponse

def index(request):
    return HttpResponse('Page of "women" application')

def categories(request, category_id):
    return HttpResponse(f'<h1>Categories page</h1><p>{category_id}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Archive by year</h1><p>{year}</p>')
