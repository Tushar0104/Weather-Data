from rest_framework import serializers
from cityweather.models import *
class WeatherDataSerializer(serializers.ModelSerializer):
   class Meta:
        model = weatherData
        fields = "__all__"
