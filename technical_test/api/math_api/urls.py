from django.urls import path, include
from rest_framework import routers
from api.math_api import views

app_name = "math_api"

urlpatterns = [path("", views.MathEndpoint.as_view(), name="math_endpoint")]
