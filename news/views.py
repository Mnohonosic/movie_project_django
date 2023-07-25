from django.shortcuts import render
from .models import News
from django.http import HttpResponse

# Create your views here.
def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})

def about(request):
    return HttpResponse('<h1>This is news about<h1/>')