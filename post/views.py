from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from post.models import *
import base64
import gzip
from pydub import AudioSegment

def converter_page(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    return render(request, 'pages/converterpage.html', context)



def song_create(request):
    print(request)
    if request.method == 'POST':
        songName = request.POST.get('songNameId')
        artistName = request.POST.get('artistId')
        albumName = request.POST.get('albumId')
        genre = request.POST.get('genreId')
        year = request.POST.get('yeartId')
        duration = request.POST.get('durationId')
        mp3_file = request.FILES['mp3FileId'].read()
        
        Song.objects.create(
            songName = songName,
            artistName = artistName,
            albumName = albumName,
            genre = genre,
            year = year,
            duration = duration,
            mp3_file = mp3_file
        )
        
    
    return redirect('BeatBlissApi:converter-page')
