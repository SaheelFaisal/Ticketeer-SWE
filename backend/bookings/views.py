from rest_framework import generics
from .models import Ticket, Show
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum, F

class TicketListView(generics.ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can access

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)
    

class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdminStatusView(APIView):
    permission_classes = [IsAdminUser]  # Only admin users can access

    def get(self, request):
        total_tickets_sold = Ticket.objects.count()
        total_revenue = Ticket.objects.aggregate(total=Sum(F('num_seats') * F('show__price')))['total'] or 0
        movies_playing = Show.objects.values_list('movie__title', flat=True).distinct()

        return Response({
            "total_tickets_sold": total_tickets_sold,
            "total_revenue": total_revenue,
            "movies_playing": list(movies_playing),
        })