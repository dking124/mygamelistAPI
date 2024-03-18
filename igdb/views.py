from django.shortcuts import render
from django.http import HttpResponse
from .igdbwrapper import *

# Create your views here.

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

