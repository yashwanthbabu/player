from django.db import models




class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField(max_length=250)

    def __str__(self):
        return self.artist + " " + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album , on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')

    def __str__(self):
        return self.song_title
