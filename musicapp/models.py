from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)

class Song(models.Model):
    title=models.CharField(max_length=100)
    date_released=models.DateField(auto_now_add=True, null=True)
    likes=models.IntegerField(null=True,)
    artise_id=models.ForeignKey(Artiste, verbose_name=_("artiste"), on_delete=models.CASCADE)

class Lyric(models.Model):
    content=models.CharField(max_lenggth=100)
    song_id=models.OneToOneField(Song, verbose_name=_("song"), on_delete=models.CASCADE)