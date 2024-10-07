from django.urls import path
from django.conf.urls.static import static
from setup import settings

from playlist.views import MusicaCreateView, MusicaDeleteView, MusicaDetailView, MusicaListView, MusicaUpdateView, PlaylistCreateView, PlaylistDeleteView, PlaylistDetailView, PlaylistListView, PlaylistUpdateView

urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist_list'),
    path('create/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist_update'),
    path('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist_delete'),

    path('musicas/', MusicaListView.as_view(), name='musica_list'),
    path('musicas/<int:pk>/', MusicaDetailView.as_view(), name='musica_detail'),
    path('musicas/create/', MusicaCreateView.as_view(), name='musica_create'),
    path('musicas/<int:pk>/edit/', MusicaUpdateView.as_view(), name='musica_update'),
    path('musicas/<int:pk>/delete/', MusicaDeleteView.as_view(), name='musica_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

