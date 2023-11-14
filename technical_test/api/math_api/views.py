from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .math_functions import numbers_option, one_number


# Create your views here.
@api_view(["GET"])
def math_endpoint(request):
    if request.method == "GET" and request.GET.get("numbers"):
        data = numbers_option(request)
        return Response(data)

    if request.method == "GET" and request.GET.get("number"):
        data = one_number(request)
        return Response(data)
    return Response(status.HTTP_404_NOT_FOUND)
