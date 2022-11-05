from django.urls import path, include
from rest_framework import routers
from . import views

from .views import ArtistViewSet, SongViewSet, LyricViewSet

router = routers.DefaultRouter()
router.register(r'artist', ArtistViewSet)
router.register(r'songs', SongViewSet)
router.register(r'lyrics', LyricViewSet)

urlpatterns = [
    path('', include(router.urls))
]
