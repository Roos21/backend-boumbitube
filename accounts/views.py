from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


from accounts.models import User
from accounts.serializers import UserSerializer

# Create your views here.

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    
    serializer_class = UserSerializer

@api_view(['POST'])
def check_email(request):
    try:
        user = User.objects.get(email=request.data['email'])
        return Response({'exist' : True}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'exist' : False}, status=status.HTTP_200_OK)

def check_user_by_email_or_username(username=None, email=None):
    try:
        user = User.objects.get(username=username, email=email)
    except User.DoesNotExist:
        user = None
        
    if user is None:
        return False
    else:
        return user

@api_view(['POST'])
def check_username(request):
    try:
        User.objects.get(username=request.data['username'])
        return Response({'exist' : True}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'exist' : False}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def create_user(request):
    
    if check_user_by_email_or_username(username=request.data['username'], email=request.data['email']):
        return Response({'exist' : True, 'message_error':'user already exist'}, status=status.HTTP_208_ALREADY_REPORTED)
    else :
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'erreur': 'Utilisateur non creer'}, status=status.HTTP_204_NO_CONTENT)

