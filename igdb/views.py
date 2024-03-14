from django.shortcuts import render
from django.http import HttpResponse
from .igdbwrapper import *

# Create your views here.
def index(request):
    url = 'https://api.igdb.com/v4/games'
    obj = 'fields cover.*; where id=103340;'
    r = wrapper(url, obj)
    return HttpResponse(r.json())

def most_popular(request):
    return