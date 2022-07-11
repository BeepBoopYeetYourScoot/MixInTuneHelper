from rest_framework import viewsets
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
