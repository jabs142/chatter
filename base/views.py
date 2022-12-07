from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This is the home page')

def room(request):
    return HttpResponse('These are our breakout rooms')