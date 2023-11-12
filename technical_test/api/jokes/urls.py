from django.urls import path, include
from rest_framework import routers
from api.jokes import views

app_name="api"

urlpatterns = [
    path('', views.random_joke, name='random_joke'),
    path('<str:select>/', views.random_chuck_or_dad_joke, name='random_chuck_joke'),
]