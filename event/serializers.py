from django.conf import settings
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from .models import Event, EventTicket, TicketInfo


class EventSerializer(serializers.ModelSerializer):
    reference_id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='event.Event.reference_id'),
        read_only=True)
    ticketInfo = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='event.TicketInfo.reference_id'),
        read_only=True)
    class Meta:
        model = Event
        fields = ['reference_id','title','date','takePlaceAt','image','ticketInfo']

class TicketInfoSerializer(serializers.ModelSerializer):
    reference_id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='event.TicketInfo.reference_id'),
        read_only=True)
    class Meta:
        model = TicketInfo
        fields = ['reference_id','available_tickets','price','vip_price']
        

class EventTicketSerializer(serializers.ModelSerializer):
    reference_id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='event.EventTicket.reference_id'),
        read_only=True)
    event = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field='event.Event.reference_id'),
        read_only=True)
    buyer = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(source_field=f'{settings.AUTH_USER_MODEL}.reference_id'),
        read_only=True)
    
    class Meta:
        model = EventTicket
        fields = ['reference_id', 'event', 'buyer', 'purchase_date', 'is_reserved','is_vip', 'is_big', 'is_payed']