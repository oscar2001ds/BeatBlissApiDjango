from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from post.models import *
import base64
import gzip
from pydub import AudioSegment

def converter_page(request):
    songs = Song.objects.all()
    albums = Album.objects.all()
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    context = {
        'songs': songs,
        'albums': albums,
        'artists':artists,
        'genres':genres,
    }
    return render(request, 'pages/converterpage.html', context)

def artist_create(request):
    if request.method == 'POST':
        artistName = request.POST.get('artistNameId')
        artistImg = request.FILES['artistImgId'].read()
        artistDesc = request.POST.get('artistDescId')
        
        Artist.objects.create(
            artistName=artistName,
            artistImg=artistImg,
            artistDesc=artistDesc,
        )
         
    return redirect('BeatBlissApi:converter-page')
        
def genre_create(request):
    if request.method == 'POST':
        genreName = request.POST.get('genreNameId')
        allGenres = Genre.objects.all()
        
        for genre in allGenres:
            if genreName == genre.genreName:
                print('Genre already exists')
                return redirect('BeatBlissApi:converter-page')
        
        print('Genre does not exist')
        Genre.objects.create(
            genreName=genreName,
        )
        
    return redirect('BeatBlissApi:converter-page')

def song_create(request):
    if request.method == 'POST':
        songName = request.POST.get('songNameId')
        songImg = request.FILES['songImgId'].read()
        artistName = Artist.objects.get(artistName=request.POST.get('artistId'))
        genre = Genre.objects.get(genreName=request.POST.get('genreId'))
        year = request.POST.get('yeartId')
        mp3_file = SongFile.objects.create(songName=songName,binary_file = request.FILES['mp3FileId'].read())
        
        Song.objects.create(
            songName = songName,
            songImg = songImg,
            artistName = artistName,
            genre = genre,
            year = year,
            mp3_file = mp3_file
        )
          
    return redirect('BeatBlissApi:converter-page')

def album_create(request):
    if request.method == 'POST':
        albumName = request.POST.get('albumSelected')
        if albumName == 'newAlbum':
            albumName = request.POST.get('newAlbumName')
        songIds = request.POST.getlist('selected_songs')
        songs = []
        for songId in songIds:
            songs.append(Song.objects.get(id=songId))
        
        album,created = Album.objects.update_or_create(
            albumName=albumName,
        )
        if not created:
            album.songs.set(songs)
            
        if 'albumImgId' in request.FILES:
            album.albumImg = request.FILES['albumImgId'].read()
        
        if request.POST['albumDescId'] != '':
            album.albumDesc = request.POST['albumDescId']
            
        album.save()
    return redirect('BeatBlissApi:converter-page')
