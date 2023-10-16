from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from post.models import Song, SongFile, Album, Artist, Genre, User
from post.api.serializers import PostSerializer, SongFileSerializer, AlbumSerializer, ArtistSerializer, GenreSerializer, UserSerializer


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Song.objects.all()

class SongFilesApiViewSet(ModelViewSet):
    serializer_class = SongFileSerializer
    queryset = SongFile.objects.all()

class AlbumApiViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class ArtistApiViewSet(ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class GenreApiViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class UserApiViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Ya existe una cuenta con el mismo correo."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Ya existe una cuenta con el mismo nombre."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)