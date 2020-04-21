from django.urls import path
from . import views



app_name = "music"
urlpatterns = [
    path('', views.MusicianIndexView.as_view(), name='index'),
    path('<str:pk>/', views.MusicianDetailView.as_view(), name='musician_detail'),
    path('<str:pk>/', views.AlbumDetailView.as_view(), name='album_detail')

]