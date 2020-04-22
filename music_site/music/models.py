from django.db import models

# Create your models here.


class Musician(models.Model):
    name = models.CharField(max_length=50)
    home_town = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
      return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    publish_date = models.DateField(null=True)
    length = models.DecimalField(decimal_places=2, max_digits=10, null=True)


    def __str__(self):
        return self.name  

