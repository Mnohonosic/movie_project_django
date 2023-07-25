from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie #schéma modelu

# Create your views here.
#def home(request):
#    return HttpResponse('<h1>This is Home :)</h1>')
def about(request):
    return HttpResponse('<h1>This is About :)</h1>')

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
      movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
     movies = Movie.objects.all() 
    
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})

def show_home(request):
   home(request)

def signup(request):
   searchTerm = request.GET.get('email')
   return render(request=request, template_name='email.html', context={'email':searchTerm})

def add_user_text(request):
   user_text = request.GET.get('user_text')

   home(request)