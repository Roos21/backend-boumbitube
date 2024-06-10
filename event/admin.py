from django.contrib import admin
from .models import Event, EventTicket,TicketInfo

class EventAdmin(admin.ModelAdmin):
    exclude = ('reference_id',)
    # Si vous préférez spécifier les champs à inclure plutôt que ceux à exclure :

    list_display = ['title','date','takePlaceAt','ticketInfo',]

class TicketInfoAdmin(admin.ModelAdmin):
    exclude = ('reference_id',)
    # Si vous préférez spécifier les champs à inclure plutôt que ceux à exclure :

    list_display = ['available_tickets','price',]
    

class EventTicketAdmin(admin.ModelAdmin):
    exclude = ('reference_id',)
    # Si vous préférez spécifier les champs à inclure plutôt que ceux à exclure :
    list_display = ['reference_id', 'event', 'buyer','purchase_date','is_vip','is_big', 'is_reserved','is_payed']

    
admin.site.register(Event, EventAdmin)
admin.site.register(TicketInfo, TicketInfoAdmin)
admin.site.register(EventTicket, EventTicketAdmin)