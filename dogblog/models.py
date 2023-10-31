from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class Dog(models.Model):
    """models for dog"""
    name = models.CharField(
        blank=False,
        null=False,
        max_length=30
        )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    breed = models.CharField(
        blank=True,
        null=True,
        max_length=30
        )

    dob = models.DateField(
        blank=True,
        null=True,
        verbose_name='Date Of Birth'
        )


class Competition(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class DogPhoto(models.Model):
    """models for dog photo"""
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE
    )

    image = CloudinaryField(
        'image',
        default='default',
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE
    )


class LikePhoto(models.Model):
    """models for like photo"""
    person = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    dog_photo = models.ForeignKey(
        DogPhoto,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )