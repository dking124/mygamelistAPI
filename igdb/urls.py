from django.urls import path, include

from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("popular/", views.most_popular, name="most_popular"),
    path("recently-released/", views.recently_released, name="recently-released"),
    path("released-soon/", views.released_soon, name="released-soon"),
    path("search/", views.search, name="search"),
    path("api/token/", TokenObtainPairView.as_view(), name="token"),
    path("api/user/", views.UserDetails.as_view(), name="user-details"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("api/games/", views.GameListCreate.as_view(), name='game-list-create'),
    path("api/games/<int:pk>/", views.GameRetrieveUpdateDestroy.as_view(), name='game-retrieve-update-destroy'),
    path("api/register/", views.register.as_view(), name="register"),
    path("api-auth/", include("rest_framework.urls")),
]