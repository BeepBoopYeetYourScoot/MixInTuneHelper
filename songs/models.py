from django.db import models
from authors.models import Author
from tuning.models import Tune


class Song(models.Model):
    authors = models.ManyToManyField(Author, related_name='songs')
    camelot_tune = models.ForeignKey(Tune, on_delete=models.DO_NOTHING, related_name='songs')

    name = models.CharField(max_length=200)  # song -> .
    spotify_id = models.CharField(max_length=200)

    # Other characteristics of a song according to Spotify

    bpm = models.PositiveSmallIntegerField(verbose_name='beats_per_minute')  # features -> tempo
    duration = models.DurationField()  # features -> duration_ms

    popularity = models.PositiveSmallIntegerField()  # song -> .
    energy = models.PositiveSmallIntegerField()  # features -> .
    danceability = models.PositiveSmallIntegerField()  # features -> .
    happiness = models.PositiveSmallIntegerField()  # features -> .
    acousticness = models.PositiveSmallIntegerField()  # features -> .
    instrumentalness = models.PositiveSmallIntegerField()  # features -> .
    liveness = models.PositiveSmallIntegerField()  # features -> .

    def __str__(self):
        return ', '.join(self.authors.all().values_list('name', flat=True)) + ' : ' + self.name
