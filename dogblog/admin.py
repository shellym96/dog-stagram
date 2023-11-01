from django.contrib import admin
from .models import Dog, Competition, DogPhoto, LikePhoto


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'breed', 'dob')


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(DogPhoto)
class DogPhotoAdmin(admin.ModelAdmin):
    list_display = ('dog', 'competition')


@admin.register(LikePhoto)
class LikePhotoAdmin(admin.ModelAdmin):
    list_display = ('person', 'dog_photo')