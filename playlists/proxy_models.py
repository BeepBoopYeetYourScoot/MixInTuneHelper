from django.db import models
import spotipy
from .models import Playlist


class SpotifyPlaylistProxy(Playlist):
    max_track_count = 100

    class Meta:
        proxy = True

    @property
    def total_duration(self) -> dict[str: models.DurationField]:
        return self.songs.all().aggregate(models.Sum('duration', output_field=models.DurationField()))

    @property
    def _spotify_client(self):
        return spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials())

    def _get_total_song_count(self, playlist_id):
        return self._spotify_client.playlist_items(playlist_id, fields='total')['total']

    def _get_playlist_tracks(self, playlist_id):
        total_song_count = self._get_total_song_count(playlist_id)
        if total_song_count <= self.max_track_count:
            return self._spotify_client.playlist_items(playlist_id)['items']  # list
        else:
            offset = 0
            playlist_tracks = []
            while total_song_count // self.max_track_count > 0:
                playlist_tracks.extend(self._spotify_client.playlist_items(playlist_id,
                                                                           limit=self.max_track_count,
                                                                           offset=offset)['items'])
            return playlist_tracks

    def load_playlist_tracks_to_database(self, playlist_id):
        track_description_template = {
            'track_id': {
                'artists': [],  # list of tracks' artists
                'features': {}  # object with tracks' features
            }
        }
        track_ids_list = [track_object['track']['id'] for track_object in self._get_playlist_tracks(playlist_id)]
        if len(track_ids_list) <= self.max_track_count:
            track_ids_string = ','.join(track_ids_list)

        features = self._spotify_client.audio_features(track_ids_string)
