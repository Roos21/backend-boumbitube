from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User


from .models import Event, EventTicket, TicketInfo
from .serializers import EventSerializer, EventTicketSerializer, TicketInfoSerializer
# Create your views here.

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(date__gt=timezone.now()).order_by('date')
    serializer_class = EventSerializer
    
class Get10ListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.filter(date__gt=timezone.now()).order_by('date')
    if queryset.count() > 10:
        queryset = queryset[:10]
    serializer_class = EventSerializer
    
class EventDetails(generics.RetrieveAPIView):
    
    serializer_class = EventSerializer
    
    def get_queryset(self):
        return Event.objects.all()
    
class EventDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = EventSerializer
    
    def get_queryset(self):
        return Event.objects.all()
    
class TicketInfoCreateView(generics.CreateAPIView):
    queryset = TicketInfo.objects.all()
    serializer_class = TicketInfoSerializer
    
    
class TicketInfoView(generics.ListAPIView):
    queryset = TicketInfo.objects.all()
    serializer_class = TicketInfoSerializer
    
class TicketInfoUpdate(generics.RetrieveUpdateAPIView):
    queryset = TicketInfo.objects.all()
    serializer_class = TicketInfoSerializer
    
class EventTicketView(generics.ListAPIView):
    queryset = EventTicket.objects.all()
    serializer_class = EventTicketSerializer
    
class EventTicketCreateView(generics.CreateAPIView):
    queryset = EventTicket.objects.all()
    serializer_class = EventTicketSerializer
    
# API VIEWS
class EventCreateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ReservationTicketView(APIView):
    def post(self, request, *args, **kwargs):
        print("Data received from client : ", request.data)
        print(User.objects.get(reference_id=request.data['buyer']))
        data = {
            "is_reserved": True,
            "reservation_expiry": "2024-06-09T12:00:00Z",
            "is_vip": True,
            "is_big": False
        }
        try :
            r = EventTicket.objects.get(
                Q(buyer=User.objects.get(reference_id=request.data['buyer']))&
                Q(event=Event.objects.get(reference_id=request.data['event']))
                )
            return Response({'message_error':'You have already make this reservation'}, status=status.HTTP_208_ALREADY_REPORTED)

        except EventTicket.DoesNotExist:
            serializer = EventTicketSerializer(data=request.data)
            if serializer.is_valid():
                reservation = serializer.save()
                reservation.event = Event.objects.get(reference_id=request.data['event'])
                reservation.buyer = User.objects.get(reference_id=request.data['buyer'])
                    
                reservation.save()
                reservation.reserve_ticket()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # En cas de mauvaise formulation de la requete de reservation
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #