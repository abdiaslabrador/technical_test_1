from django.urls import path, include
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r'programmers', views.ProgrammerViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]
urlpatterns = [
    path('', views.random_joke, name='random_joke'),
    # path('<str:select>/', views.joke_select_type, name='random_joke'),
    path('Chuck/', views.random_chuck_joke, name='random_chuck_joke'),
    path('Dad/', views.random_dad_joke, name='random_dad_joke'),
    path('math_endpoint/', views.math_endpoint, name='math_endpoint')
]