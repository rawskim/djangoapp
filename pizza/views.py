from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Witaj  w barze Pizza!")
    return render(request, 'pizza/index.html')

def news(request):
    #return HttpResponse("Nowości")
    return render(request, 'pizza/news.html')
