from django.db import models
import uuid

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    poster_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
