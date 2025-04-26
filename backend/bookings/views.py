from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated

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