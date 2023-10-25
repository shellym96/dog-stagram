from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'dogstagram/home.html')

def photos(request):
    return render(request, 'dogstagram/photos.html')

def competition(request):
    return render(request, 'dogstagram/competition.html')




