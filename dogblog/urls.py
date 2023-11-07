from django.urls import path, include
from . import views
from .views import home, photos, competition
urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('competition/', views.competition, name='competition'),
    path('accounts/', include('allauth.urls')),
    path('like/<int:id>', views.LikeDogPhoto.as_view(), name='photo_like'),
    
]