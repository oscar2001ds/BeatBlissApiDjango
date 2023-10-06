from django.contrib import admin
from post.models import Song

# Register your models here.
@admin.register(Song)

class PostAdmin(admin.ModelAdmin):
    list_display = ['songName', 'artistName', 'albumName', 'genre', 'year', 'duration', 'created_at', 'updated_at']
    list_display_links = ['songName']
    search_fields = ['songName']
    
    
