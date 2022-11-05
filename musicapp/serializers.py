from . models import  Song, Artiste, Lyric
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'
