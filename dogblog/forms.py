from .models import DogPhoto
from django import forms


class DogPhotoForm(forms.ModelForm):
    class Meta:
        model = DogPhoto
        fields = ('image',)
