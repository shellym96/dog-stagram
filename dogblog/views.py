from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Dog, Competition, DogPhoto, LikePhoto
from .forms import DogPhotoForm, DogForm


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
            messages.success(
                request,
                f"{dog_photo.dog.name} has been entered into the "
                f"{dog_photo.competition} competition! Good Luck!"
            )
            return HttpResponseRedirect(reverse('competition'))
        messages.error(request, 'An error has occured. Please try again.')

    else:
        form = DogPhotoForm()
        form.fields['dog'].queryset = Dog.objects.filter(owner=request.user)

    context = {
        'form': form,
    }
    return render(request, 'add_photo.html', context)


def competition(request):
    photos = DogPhoto.objects.all().order_by('competition')
    context = {
        'photos': photos,
    }
    return render(request, 'competition.html', context)


def edit_photo(request, photo_id):
    photo = get_object_or_404(DogPhoto, id=photo_id)
    if photo.dog.owner != request.user:
        messages.error(request, 'Not Authorised To Perfom This Action!')
        return redirect(reverse('competition'))
    if request.method == 'POST':
        form = DogPhotoForm(request.POST, request.FILES, instance=photo)
        form.fields['dog'].queryset = Dog.objects.filter(owner=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Photo of {photo.dog.name} has been updated"
            )
            return HttpResponseRedirect(reverse('competition'))
        messages.error(request, 'An error has occured. Please try again.')
    form = DogPhotoForm(instance=photo)
    form.fields['dog'].queryset = Dog.objects.filter(owner=request.user)
    context = {
        'form': form
    }
    return render(request, 'edit_photo.html', context)


def delete_photo(request, photo_id):
    photo = get_object_or_404(DogPhoto, id=photo_id)
    if photo.dog.owner != request.user:
        messages.error(request, 'Not Authorised To Perfom This Action!')
        return redirect(reverse('competition'))
    photo.delete()
    messages.success(request, f"Photo of {photo.dog.name} has been deleted")
    return HttpResponseRedirect(reverse('competition'))


class LikeDogPhoto(View):
    def post(self, request, id):
        photo = get_object_or_404(DogPhoto, id=id)

        if photo.likes.filter(id=request.user.id).exists():
            photo.likes.remove(request.user)
            messages.info(
                self.request, f"You no longer like {photo.dog.name}'s photo"
            )
        else:
            photo.likes.add(request.user)
            messages.info(self.request, f"You liked {photo.dog.name}'s photo")

        return HttpResponseRedirect(reverse('competition'))


def add_dog(request):
    form = DogForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user
            dog.save()
            messages.success(request, f"{dog.name} has been added!")
            return HttpResponseRedirect(reverse('home'))
    context = {
        "form": form,
    }

    return render(request, 'add_dog.html', context)
