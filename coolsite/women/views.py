from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *

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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Post add error')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add article'})

def contact(request):
    return HttpResponseNotFound('Contact us')

def login(request):
    return HttpResponseNotFound('Login')

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
               'posts': posts,
               'menu': menu,
               'title': 'Categories',
               'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)