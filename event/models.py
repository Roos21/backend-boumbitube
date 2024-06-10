from django.db import models
from django.utils import timezone
from django.conf import settings

from accounts.models import Subscriber, TimeStamps, User
from hashid_field import HashidAutoField

class TicketInfo(TimeStamps):
    reference_id = HashidAutoField(primary_key=True, unique=True)
    available_tickets = models.IntegerField()
    price = models.IntegerField(default=0, null=True, blank=True)
    vip_price = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.reference_id}'

class Event(TimeStamps):
    
    reference_id = HashidAutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    takePlaceAt = models.CharField(max_length=255)
    owner = models.ManyToManyField("accounts.User", blank=True, related_name='organizer_event')
    image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    description = models.TextField(max_length=2048,blank=True, null=True, default="Lorem ipsum dolor sit amet, consectetur adip euismod er at, sed diam nonumy eirmod tempor incididunt ut labore et dolore magna aliqu compliance et justo euismod. Ut enim ad minim veniam et aliqu")
    # Modification du champ ticketInfo
    ticketInfo = models.ForeignKey('TicketInfo', on_delete=models.CASCADE, blank=True, null=True)
    guestList = models.ManyToManyField(Subscriber, related_name='invited_to_event', blank=True)
    
    
    
    def invite_subscriber(self, subscriber):
        self.guestList.add(subscriber)

    # Ajout de méthodes pour l'événement
    def get_available_tickets(self):
        return self.ticketInfo.available_tickets

    def get_attending_subscribers(self):
        return self.guestList.all()
    def __str__(self):
        return self.title

class EventTicket(TimeStamps):
    
    reference_id = HashidAutoField(primary_key=True, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets', blank=True,null=True)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,null=True)
    purchase_date = models.DateTimeField(default=timezone.now)
    is_reserved = models.BooleanField(default=False)
    reservation_expiry = models.DateTimeField(blank=True, null=True)
    
    is_vip = models.BooleanField(default=False)
    is_big = models.BooleanField(default=False)
    
    is_payed = models.BooleanField(default=False)

    

    def reserve_ticket(self, reservation_time=(48 * 60)):
        self.is_reserved = True
        self.event.ticketInfo.available_tickets -= 1
        self.reservation_expiry = timezone.now() + timezone.timedelta(minutes=reservation_time)
        self.save()
        self.event.ticketInfo.save()

    def cancel_reservation(self):
        self.is_reserved = False
        self.reservation_expiry = None
        self.save()

    def is_reservation_expired(self):
        if self.is_reserved and self.reservation_expiry:
            return timezone.now() > self.reservation_expiry
        return False
