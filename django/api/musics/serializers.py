from rest_framework import serializers
from .models import Music, Artist, Comment

# 모델폼과 비슷하게 생김
# 중간에 껴서 통역 역할

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist',]
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']
        
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'music_set',]
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content',]