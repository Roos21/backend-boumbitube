from django.urls import path
from .views import *

app_name = 'event'

urlpatterns = [
    path('', EventListCreateAPIView.as_view(), name="list-events"),
    path('get-ten/', Get10ListCreateAPIView.as_view(), name="last-events"),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('<str:pk>/details', EventDetails.as_view(), name="event-details"),
    path('<str:pk>/delete', EventDestroy.as_view(), name="event-delete"),
    path('<str:pk>/update', EventDestroy.as_view(), name="event-delete"),
    
    path('ticket/create', TicketInfoCreateView.as_view(), name="ticket-info-create"),
    path('ticket/', TicketInfoView.as_view(), name="ticket-info-list"),
    path('ticket/update', TicketInfoUpdate.as_view(), name="ticket-info-update"),
    
    #
    path('event-ticket/', EventTicketView.as_view(), name="event-ticket"),
    path('event-ticket/reservation', ReservationTicketView.as_view(), name="event-ticket-create"),
]
