from django.conf import settings
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from accounts.models import Artist, ProductionHouse, Subscriber, User

# class UserSerializer(serializers.ModelSerializer):
#     reference_id = serializers.PrimaryKeyRelatedField(
#         pk_field=HashidSerializerCharField(source_field='accounts.User.reference_id'),
#         read_only=True)
#     class Meta:
#         model = User
#         fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class SubscriberSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
         pk_field=HashidSerializerCharField(source_field=f'{settings.AUTH_USER_MODEL}.reference_id'),
         read_only=True)
    class Meta:
        model = Subscriber
        fields = ['user', 'alias', 'civilStatus','dateOfBirth','phoneNumber']
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['alias', 'civilStatus', 'dateOfBirth', 'phoneNumber', 'firstHitSingle', 'isPremiem', 'bio', 'aboutMe']


class ProductionHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionHouse
        fields = ['name', 'address', 'foundingYear', 'founder', 'description', 'website']



