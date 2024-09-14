from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .igdbwrapper import *
from .models import Game, CustomUser
from .serializers import GameSerializer, CustomUserSerializer

# Create your views here.

# CRUD endpoints
class GameListCreate(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

class UserDetails(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)

# Views that will be used to create homepage of mygamelist
def most_popular(request):
    r = wrapper('https://api.igdb.com/v4/games',
                'fields name,total_rating,total_rating_count,cover.url; where total_rating_count>100 ; sort total_rating desc;')
    return HttpResponse(r)

def recently_released(request):
    body = 'fields game.name,game.total_rating,game.total_rating_count,game.cover.url; where date < ; sort date desc;'
    r = release(body)
    return HttpResponse(r)

def released_soon(request):
    body = 'fields game.name,game.total_rating,game.total_rating_count,game.cover.url; where date > ; sort date asc;'
    r = release(body)
    return HttpResponse(r)

@api_view(['POST'])
@permission_classes([AllowAny])
def search(request):
    r = wrapper('https://api.igdb.com/v4/games',
                'search ' + '"' + request.data + '"; fields name;')
    return Response(r)

# Register endpoint
class register(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
