from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)  # TMDb's vote_average
    vote_count = models.IntegerField(null=True, blank=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    backdrop_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

