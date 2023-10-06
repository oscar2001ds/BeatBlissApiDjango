from rest_framework.viewsets import ModelViewSet
from post.models import Song
from post.api.serializers import PostSerializer


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Song.objects.all()
    