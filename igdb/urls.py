from django.urls import path

from . import views

urlpatterns = [
    path("popular/", views.most_popular, name="most_popular"),
    path("recently_released/", views.recently_released, name="recently_released"),
    path("released_soon/", views.released_soon, name="released_soon")
]