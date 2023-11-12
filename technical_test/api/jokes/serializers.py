from rest_framework import serializers
from .models import JokeModel

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JokeModel
        fields = ['id', 'joke']