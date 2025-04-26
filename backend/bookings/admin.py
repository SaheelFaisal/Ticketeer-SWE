from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'show', 'user', 'num_seats', 'booking_time', 'barcode')
    search_fields = ('show__movie_name', 'user__username', 'barcode')
    list_filter = ('show',)
