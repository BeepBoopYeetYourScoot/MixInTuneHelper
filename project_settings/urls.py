from django.contrib import admin
from django.urls import path, include
from playlists.urls import playlist_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include(playlist_urls))
]
