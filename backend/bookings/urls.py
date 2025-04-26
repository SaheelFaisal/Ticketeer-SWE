from django.urls import path
from .views import TicketListView, TicketCreateView

urlpatterns = [
    path('tickets/list/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
]
