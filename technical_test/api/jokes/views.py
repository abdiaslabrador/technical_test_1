from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JokeModel
from .serializers import JokeSerializer
from rest_framework.views import APIView

# from drf_yasg.utils import swagger_auto_schema

from .joke_functions import (
    random_joke_get_method,
    random_chuck_joke_function,
    random_dad_joke_function,
)


class RandomJoke(APIView):
    def get(self, request, format=None):
        """
        Obtiene un chiste aleatorio
        """
        joke = random_joke_get_method()
        return Response(joke, status=200)

    def post(self, request, format=None):
        """
        Crea un chiste
        """
        joke = {"joke": request.GET.get(list(request.GET.dict())[0])}
        serializer = JokeSerializer(data=joke)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, format=None):
        id_joke = request.GET.get("number")
        joke_data = request.GET.get("joke")

        try:
            joke = JokeModel.objects.get(id=id_joke)
        except JokeModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = JokeSerializer(joke, data={"id": id_joke, "joke": joke_data})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, format=None):
        id_joke = request.GET.get("number")

        try:
            joke = JokeModel.objects.get(id=id_joke)
        except JokeModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = {}
        operation = joke.delete()
        if operation:
            data["success"] = "successful deleted"
        else:
            data["failure"] = "failure deleted"
        return Response(data)


class RandomChuckOrDadJoke(APIView):
    def get(self, request, select, format=None):
        if select == "Chuck":
            joke = random_chuck_joke_function()
            return Response(joke, status=200)
        elif select == "Dad":
            joke = random_dad_joke_function()
            return Response(joke, status=200)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
