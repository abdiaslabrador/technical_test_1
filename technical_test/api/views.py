
from math import lcm as mcm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
import requests
from .models import JokeModel
from .serializers import JokeSerializer
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def random_joke(request):
	joke = {}
	if request.method == 'GET':
		r = requests.get('https://api.chucknorris.io/jokes/random').json()
		joke = {'joke' : r["value"]}
		return Response(joke)
	
	elif request.method == 'POST':
		# serializer = JokeSerializer(data=request.data)
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
		

# @api_view(['GET'])
# def joke_select_type(request, select):
# 	if select == "Chuck":
# 		r = requests.get('https://api.chucknorris.io/jokes/random').json()
# 		joke = {'chuck_joke' : r["value"]}
# 		return Response(joke)
	
# 	if select == "Dad":
# 		url = 'https://icanhazdadjoke.com/'
# 		headers = {
# 		'Accept': 'application/json',
# 		}
# 		r = requests.get(url, headers=headers).json()
		
# 		joke = {'dad_joke' : r["joke"]}
		
# 		return Response(joke)

@api_view(['GET'])
def random_chuck_joke(request):
	r = requests.get('https://api.chucknorris.io/jokes/random').json()
	joke = {'chuck_joke' : r["value"]}
	
	return Response(joke)


@api_view(['GET'])
def random_dad_joke(request):
    url = 'https://icanhazdadjoke.com/'
    headers = {
    'Accept': 'application/json',
    }
    r = requests.get(url, headers=headers).json()
    
    joke = {'dad_joke' : r["joke"]}
	
    return Response(joke)

@api_view(['GET'])
def math_endpoint(request):

	if request.method == 'GET' and request.GET.get('numbers'):
		list_chart = request.GET.get('numbers').split(sep=",")
		# list_chart=list_chart.split(sep=",")
		array = []
		for i in list_chart:
			array.append(int(i))

		result = mcm(*array)
		data={
				'numbers': array,
				'result': result
			}
		return Response(data)	
	
	if request.method == 'GET' and request.GET.get('number'):
		number=int(request.GET.get('number'))
		data={
				'number': number,
				'result': number + 1
			}
		return Response(data)
	return Response("no hay numbers")