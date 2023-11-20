from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competition/', views.competition, name='competition'),
    path('accounts/', include('allauth.urls')),
    path('like/<int:id>', views.LikeDogPhoto.as_view(), name='photo_like'),
    path('add_photo', views.add_photo, name='add_photo'),
    path('add_dog', views.add_dog, name='add_dog'),
    path('edit/<int:photo_id>', views.edit_photo, name='edit_photo'),
    path('delete/<int:photo_id>', views.delete_photo, name='delete_photo'),
]