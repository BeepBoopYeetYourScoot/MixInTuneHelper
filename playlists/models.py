from django.db import models
from django.db.models import Sum

from songs.models import Song
from tuning.models import Tune


class Playlist(models.Model):
    songs = models.ManyToManyField(Song, related_name='playlists')
    tunes = models.ManyToManyField(Tune, related_name='playlists')

    name = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
