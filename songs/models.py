from django.db import models
from authors.models import Author
from tuning.models import Tune


class Song(models.Model):
    authors = models.ManyToManyField(Author, related_name='songs')
    camelot_tune = models.ForeignKey(Tune, on_delete=models.DO_NOTHING, related_name='songs')

    name = models.CharField(max_length=200)
    tunebat_link = models.URLField()
    bpm = models.PositiveSmallIntegerField(verbose_name='beats_per_minute')
    duration = models.DurationField()

    # Other characteristics of a song according to tunebat.com
    popularity = models.PositiveSmallIntegerField()
    energy = models.PositiveSmallIntegerField()
    danceability = models.PositiveSmallIntegerField()
    happiness = models.PositiveSmallIntegerField()
    liveness = models.PositiveSmallIntegerField()

    def __str__(self):
        return ', '.join(self.authors.all().values_list('name', flat=True)) + ' : ' + self.name
