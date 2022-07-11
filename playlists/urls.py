from rest_framework.routers import SimpleRouter
from .views import PlaylistViewSet

router = SimpleRouter()

router.register('playlist', PlaylistViewSet)

playlist_urls = router.urls
