from django.urls import path, include
from . import views
from .views import home, photos, competition
urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos, name='photos'),
    path('competition/', views.competition, name='competition'),
    path('accounts/', include('allauth.urls')),
    path('like/<slug:slug>', views.LikePhoto.as_view(), name='post_like'),
    
]