from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('backend-admin/', admin.site.urls),
    path('event/', include("event.urls", namespace="event")),
    path('accounts/', include("accounts.urls", namespace="accounts")),
]


#Ajouter cette ligne
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

