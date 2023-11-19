from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Dog, Competition, DogPhoto, LikePhoto
from .forms import DogPhotoForm, DogForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def photos(request):
    return render(request, 'photos.html')

def add_photo(request):
    if request.method == 'POST':
        form = DogPhotoForm(request.POST, request.FILES)
        form.fields['dog'].queryset = Dog.objects.filter(owner=request.user)

        if form.is_valid():
            dog_photo = form.save(commit=False)
            dog_photo.save()

            return HttpResponseRedirect(reverse('competition'))

    else:
        form = DogPhotoForm()
        form.fields['dog'].queryset = Dog.objects.filter(owner=request.user)

    context = {
        'form': form,
    }
    return render(request, 'add_photo.html', context)


def competition(request):
    competitions = Competition.objects.all()
    photos = DogPhoto.objects.all()
    context = {
        'competitions': competitions,
        'photos': photos,
    }
    return render(request, 'competition.html', context)


def edit_photo(request, photo_id):
    photo = get_object_or_404(DogPhoto, id=photo_id)
    if request.method == 'POST':
        form = DogPhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('competition'))
    form = DogPhotoForm(instance=photo)
    context = {
        'form': form
    }
    return render(request, 'edit_photo.html', context)


class LikeDogPhoto(View):
    def post(self, request, id):
        photo = get_object_or_404(DogPhoto, id=id)

        if photo.likes.filter(id=request.user.id).exists():
            photo.likes.remove(request.user)
        else:
            photo.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('competition'))


def add_dog(request):
    form = DogForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user
            dog.save()

            return HttpResponseRedirect(reverse('home'))
    context = {
        "form": form,
    }

    return render(request, 'add_dog.html', context)




