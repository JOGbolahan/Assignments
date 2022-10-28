from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Artiste(models.Model):
    Name = models.CharField(max_length=400)
    Artiste_ID = models.IntegerField(primary_key=True)
    Followers = models.IntegerField()
    Monthly_Listeners = models.IntegerField()

    def __str__(self):
        return self.Name

class Song(models.Model):
    Song_Title = models.CharField(max_length=400)
    Date_Released = models.DateField()
    Likes = models.IntegerField()
    Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)

class Lyrics(models.Model):
    Content = models.TextField()
    Song_ID = models.OneToOneField(Song, on_delete=models.PROTECT)




