from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Musician, Album, Song

# Create your views here.

def index(request):
    return HttpResponse('Hello world you\'re at the music app home page')


class MusicianIndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'musician_list'

    def get_queryset(self):
        return Musician.objects.all()


class MusicianDetailView(generic.DetailView):
    model = Musician
    template_name = 'music/musician_detail.html'


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'music/album_detail.html'

class SongDetailView(generic.DetailView):
    model = Song
    template_name = 'music/song_detail.html'