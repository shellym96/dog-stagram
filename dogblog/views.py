from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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


class LikeDogPhoto(View):
    def post(self, request, id):
        photo = get_object_or_404(DogPhoto, id=id)

        if photo.likes.filter(id=request.user.id).exists():
            photo.likes.remove(request.user)
        else:
            photo.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('competition'))
