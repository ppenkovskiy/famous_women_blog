from django.http import HttpResponse

def index(request):
    return HttpResponse('Page of "women" application')

def categories(request):
    return HttpResponse('<h1>Categories page</h1>')