from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class View(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
    """A string representation of the model."""
        return self.title

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=550)
    genre = models.CharField(max_length=150)
    album_logo = models.ImageField(upload_to='images', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk})


