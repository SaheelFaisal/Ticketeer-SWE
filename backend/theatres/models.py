from django.db import models
from movies.models import Movie

class Theatre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - ({self.location})"

class Show(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='shows', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    language = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

    def __str__(self):
        return f"{self.movie.title} at {self.theatre.name} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"
