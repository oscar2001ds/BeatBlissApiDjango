from django.urls import path
from .views import *

app_name = 'BeatBlissApi'

urlpatterns = [
    path('converter', converter_page, name='converter-page'),
    path('song-create', song_create, name='song-create'),
 
]