from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title=models.CharField(max_length=100)
    date_released=models.DateField(auto_now_add=True, null=True)
    likes=models.IntegerField(null=True,)
    artise_id=models.ForeignKey(Artiste, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Lyric(models.Model):
    content=models.CharField(max_length=100)
    song_id=models.OneToOneField(Song, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
