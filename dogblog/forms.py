from django import forms
from .models import DogPhoto, Dog


class DateInput(forms.DateInput):
    input_type = 'date'


class DogPhotoForm(forms.ModelForm):
    class Meta:
        model = DogPhoto
        fields = ('dog', 'competition', 'image')


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'breed', 'dob')
        widgets = {
            'dob': DateInput()
        }
