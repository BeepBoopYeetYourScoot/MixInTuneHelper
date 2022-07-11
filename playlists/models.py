from django.db import models
from songs.models import Song
from tuning.models import Tune


class Playlist(models.Model):
    songs = models.ManyToManyField(Song)
    tunes = models.ManyToManyField(Tune)

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @property
    def song_count(self):
        return self.songs.all().count()
