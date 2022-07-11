from django.db import models
from django.db.models import Sum

from songs.models import Song
from tuning.models import Tune


class Playlist(models.Model):
    songs = models.ManyToManyField(Song, related_name='playlists')
    tunes = models.ManyToManyField(Tune, related_name='playlists')

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def song_count(self) -> int:
        return self.songs.all().count()

    @property
    def total_duration(self) -> dict[str: models.DurationField]:
        return self.songs.all().aggregate(Sum('duration', output_field=models.DurationField()))
