from django.urls import path
from . import views
from .views import home, photos, competition
urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('competition/', views.competition, name='competition')
    
]