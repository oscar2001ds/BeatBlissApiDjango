from django.db import models

class SongFile(models.Model):
    songName = models.CharField(max_length=100, default='')
    binary_file = models.BinaryField()
    
    def __str__(self):
        return  str(self.id)

class Artist(models.Model):
    artistName = models.CharField(max_length=100)
    artistImg = models.BinaryField()
    artistDesc = models.TextField()
    
    def __str__(self):
        return self.artistName
    
class Genre(models.Model):
    genreName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genreName

class Song(models.Model):
    songName = models.CharField(max_length=100)
    songImg = models.BinaryField()
    artistName = models.ForeignKey('Artist', on_delete=models.CASCADE) 
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    year = models.IntegerField()
    mp3_file = models.OneToOneField(SongFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.songName
    
class Album(models.Model):
    albumName = models.CharField(max_length=100)
    albumImg = models.BinaryField()
    albumDesc = models.TextField()
    songs = models.ManyToManyField(Song)
    
    def __str__(self):
        return self.albumName
    

class User(models.Model):
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True )
    email = models.CharField(max_length=100, blank=True)
    playlists = models.ManyToManyField(Album, blank=True)
    
    def __str__(self):
        return self.username
    
