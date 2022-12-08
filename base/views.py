from django.shortcuts import render
from .models import Room #import the model you want to query
# Create your views here.

def home(request):
    rooms = Room.objects.all() #querying the rooms from the database 
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room};
    return render(request, 'base/room.html', context)