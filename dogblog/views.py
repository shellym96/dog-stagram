from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import Dog, Competition, DogPhoto, LikePhoto

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photos(request):
    return render(request, 'photos.html')

def competition(request):
    competitions = Competition.objects.all()
    photos = DogPhoto.objects.all()
    context = {
        'competitions': competitions,
        'photos': photos,
    }
    return render(request, 'competition.html', context)




