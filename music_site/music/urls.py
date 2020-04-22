from django.urls import path
from . import views



app_name = "music"
urlpatterns = [
    path('', views.MusicianIndexView.as_view(), name='index'),
    path('<int:pk>/', views.MusicianDetailView.as_view(), name='musician_detail'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song_detail')

]