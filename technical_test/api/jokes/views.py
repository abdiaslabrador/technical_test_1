
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JokeModel
from .serializers import JokeSerializer
# from drf_yasg.utils import swagger_auto_schema
from .joke_functions import random_joke_get_method, random_chuck_joke_function, random_dad_joke_function

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def random_joke(request):
	
	joke = {}
	if request.method == 'GET':
		joke=random_joke_get_method()
		return Response(joke)
	
	elif request.method == 'POST':
		joke ={'joke':request.GET.get(list(request.GET.dict())[0])}
		serializer = JokeSerializer(data=joke)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)
	
	elif request.method == 'PUT':
		joke=request.GET.get('chiste')
		id_joke=request.GET.get('number')
		
		try:
			joke = JokeModel.objects.get(id=id_joke)
		except JokeModel.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)
		
		serializer = JokeSerializer(joke, data=request.GET.dict())
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=200)
		return Response(serializer.errors, status=400)

	elif request.method == 'DELETE':
		id_joke=request.GET.get('number')
		
		try:
			joke = JokeModel.objects.get(id=id_joke)
		except JokeModel.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)
		
		data = {}
		operation = joke.delete()
		if operation :
			data["success"] = "successful deleted"
		else:
			data["failure"] = "failure deleted"
		return Response(data)	
		

@api_view(['GET'])
def random_chuck_or_dad_joke(request, select):
	if select == "Chuck":
		joke = random_chuck_joke_function()
	elif select == "Dad":
		joke = random_dad_joke_function()
	else:
		{"message":"option not found"}
	return Response(joke)

