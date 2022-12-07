from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'Django support group'},
    {'id':2, 'name':'Debugging Django'},
    {'id':3, 'name':'React study group'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html',context)

def room(request):
    return render(request, 'room.html')