from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    
    path('users/',ListUserView.as_view(), name='users'),
    path('users/create',create_user, name='user-create'),

]