from rest_framework.serializers import ModelSerializer
from post.models import Song, SongFile, Album, Artist, Genre, User

class PostSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
class SongFileSerializer(ModelSerializer):
    class Meta:
        model = SongFile
        fields = '__all__'
        read_only_fields = ['id', 'binary_file']

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['id']

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        read_only_fields = ['id']

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['id']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id']