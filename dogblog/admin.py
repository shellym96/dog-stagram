from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Dog, Competition, DogPhoto, LikePhoto


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


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