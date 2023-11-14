from django.urls import path, include
from rest_framework import routers
from api.jokes import views

app_name = "jokes_api"

urlpatterns = [
    path("", views.RandomJoke.as_view(), name="random_joke"),
    path(
        "<str:select>/", views.RandomChuckOrDadJoke.as_view(), name="random_chuck_joke"
    ),
]
