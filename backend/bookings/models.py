from django.db import models
from django.contrib.auth import get_user_model
from theatres.models import Show

User = get_user_model()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    num_seats = models.PositiveIntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.show} ({self.num_seats} seats)"
