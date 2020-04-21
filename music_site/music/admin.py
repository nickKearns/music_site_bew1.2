from django.contrib import admin
from .models import Album, Musician, Song

# Register your models here.

admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Song)