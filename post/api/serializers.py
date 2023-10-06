from rest_framework.serializers import ModelSerializer
from post.models import Song

class PostSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']