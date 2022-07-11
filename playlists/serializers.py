from rest_framework import serializers
from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    song_count = serializers.IntegerField()
    total_duration = serializers.DurationField()

    class Meta:
        model = Playlist
        fields = '__all__'
