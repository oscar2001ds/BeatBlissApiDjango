from django.urls import path
from .views import *

app_name = 'BeatBlissApi'

urlpatterns = [
    path('converter', converter_page, name='converter-page'),
    path('song-create', song_create, name='song-create'),
    path('album-create', album_create, name='album-create'),
    path('artist-create', artist_create, name='artist-create'),
    path('genre-create', genre_create, name='genre-create'),
 
]