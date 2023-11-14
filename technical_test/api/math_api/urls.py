from django.urls import path, include
from rest_framework import routers
from api.math_api import views

app_name="api"

urlpatterns = [
    path('', views.math_endpoint, name='math_endpoint')
]