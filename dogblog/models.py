from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


class Dog(models.Model):
    """models for dog"""
    name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        unique=False)

    owner = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=1,
        max_length=30,
        verbose_name='Owner',
        unique=False)

    breed = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        unique=False)

    dob = models.DateField(
        blank=True,
        null=True,
        verbose_name='DOB')


class User(models.Model):
    """models for user"""
    username = models.CharField(
        blank=True,
        null=True,
        max_length=8,
        unique=True,
        verbose_name=' Username '
    )

    email = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        unique=False,
        verbose_name='Email'
    )


class LikePhoto(models.Model):
    """models for like photo"""
    person = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=1,
        verbose_name='Person'
    )

    dog_photo = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=1,
        verbose_name='Dog Photo'
    )

    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )
    

class DogPhoto(models.Model):
    """models for dog photo"""
    dog = models.ForeignKey(
        Dog,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=1
    )

    """ ALT HERE """

    image = models.ImageField(
        upload_to='dog_photo',
        default='default.jpg',
        verbose_name='Image'
    )

    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )
    
    competition = models.ForeignKey(
        DogPhoto,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=1,
        verbose_name='Competition'
    )

class Competition(models.Model):
    name = models.CharField(
        DogPhoto,
        blank=True,
        null=True,
        max_length=15,
        verbose_name='Name',
        unique=True
    )

    created_at