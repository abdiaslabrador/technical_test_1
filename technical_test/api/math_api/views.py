from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .math_functions import numbers_option, one_number
from rest_framework.views import APIView


# Create your views here.
class MathEndpoint(APIView):
    def get(self, request, format=None):
        if request.GET.get("numbers"):
            data = numbers_option(request)
            return Response(data)

        if request.GET.get("number"):
            data = one_number(request)
            return Response(data)
        return Response(status.HTTP_404_NOT_FOUND)
