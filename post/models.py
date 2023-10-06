from django.db import models

# Create your models here.
class Song(models.Model):
    songName = models.CharField(max_length=100)
    artistName = models.CharField(max_length=100)
    albumName = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    duration = models.IntegerField()
    mp3_file = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    
    def __str__(self):
        return self.songName