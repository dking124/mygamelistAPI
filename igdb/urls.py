from django.urls import path

from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("popular/", views.most_popular, name="most_popular"),
    path("recently_released/", views.recently_released, name="recently_released"),
    path("released_soon/", views.released_soon, name="released_soon"),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/games/", views.GameListCreate.as_view(), name='game-list-create'),
    path("api/games/<int:pk>/", views.GameRetrieveUpdateDestroy.as_view(), name='game-retrieve-update-destroy'),
    path("api/register/", views.register.as_view(), name="register"),
    path("api/sign_in/", views.sign_in, name="sign_in"),
]