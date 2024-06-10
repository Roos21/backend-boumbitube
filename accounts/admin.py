from django.contrib import admin

from accounts.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # Exclure le champ reference_id
    exclude = ('reference_id',)

admin.site.register(User, UserAdmin)