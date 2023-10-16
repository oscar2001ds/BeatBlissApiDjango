from django.contrib import admin
from post.models import Song, SongFile, Album, Artist, Genre, User

# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id','songName', 'artistName', 'genre', 'year', 'mp3_file' , 'created_at', 'updated_at']
    list_display_links = ['songName']
    search_fields = ['songName']
    
@admin.register(SongFile)
class SongFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'songName', 'binary_file']
    list_display_links = ['id']
    search_fields = ['id']
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id','artistName', 'artistDesc']
    list_display_links = ['artistName']
    search_fields = ['artistName']
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id','albumName', 'albumDesc']
    list_display_links = ['albumName']
    search_fields = ['albumName']
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id','genreName']
    list_display_links = ['genreName']
    search_fields = ['genreName']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','password', 'email']
    list_display_links = ['username']
    search_fields = ['username']