from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Dog, Competition, DogPhoto, LikePhoto
from .forms import DogPhotoForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photos(request):
    return render(request, 'photos.html')

def add_photo(request):
    if request.method == 'POST':
        dog_id = request.POST.get('dog')
        competition_id = request.POST.get('competition')
        form = DogPhotoForm(request.POST, request.FILES)
        print(request.FILES)
        dog = get_object_or_404(Dog, id=dog_id)
        competition = get_object_or_404(Competition, id=competition_id)

        if form.is_valid():
            dog_photo = form.save(commit=False)
            dog_photo.dog = dog
            dog_photo.competition = competition
            dog_photo.save()

            return HttpResponseRedirect(reverse('competition'))

    else:
        form = DogPhotoForm()

    # Fetch dogs and competitions to pass to the template
    dogs = Dog.objects.all()
    print("dogs", dogs)
    competitions = Competition.objects.all()
    print("competitions", competitions)

    return render(request, 'add_photo.html', {'form': form, 'dogs': dogs, 'competitions': competitions})


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



