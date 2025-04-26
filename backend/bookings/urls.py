from django.urls import path
from .views import TicketListView, TicketCreateView, AdminStatusView

urlpatterns = [
    path('tickets/list/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('admin/status/', AdminStatusView.as_view(), name='admin-status'),
]
