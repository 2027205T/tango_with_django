from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br/><br/> <a href='/rango/about'>About page</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <br /><br /> <a href='/rango/'>Return to main page</a>")
