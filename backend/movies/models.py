from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    genres = models.TextField(blank=True, default="")  # Store genre names as a comma-separated string
    overview = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)  # TMDb's vote_average
    vote_count = models.IntegerField(null=True, blank=True)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    backdrop_url = models.URLField(max_length=500, blank=True, null=True)
    cast = models.TextField(blank=True, null=True, default="")  # Store comma-separated cast names

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.first_name} {self.user.last_name}"
