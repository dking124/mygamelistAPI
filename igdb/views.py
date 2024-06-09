#from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from .igdbwrapper import *
from .models import Game, CustomUser
from .serializers import GameSerializer, CustomUserSerializer

# Create your views here.

# Django REST Framework 
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

# Views that will be used to create homepage of mygamelist
def most_popular(request):
    r = wrapper('https://api.igdb.com/v4/games',
                'fields name,total_rating,total_rating_count; where total_rating_count>100 ; sort total_rating desc;')
    return HttpResponse(r)

def recently_released(request):
    body = 'fields *; where date < ; sort date desc;'
    r = release(body)
    return HttpResponse(r)

def released_soon(request):
    body = 'fields *; where date > ; sort date asc;'
    r = release(body)
    return HttpResponse(r)

# Register/Signin forms

class register(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

def sign_in(request):
    return

