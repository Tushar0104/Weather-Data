from cityweather.models import city, weatherData, weatherUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from cityweather.serializer import *
import requests


@api_view(["GET"])
def get_weather(request):
    try:
        city_obj = city.objects.filter(id_disable=False)
        print(f" {city_obj.count()}")
        for x in city_obj:
            print(f"adsffsssf")
            lat = x.latitude
            long = x.longitude
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=2997a532492c8e3520c064708bd8dc3a'
            result = requests.get(url).json()
            print(f"asdfv {result}")
            weatherData.objects.update_or_create(city= x.name,defaults=dict(
                weather = result['weather'][0]['main'],
                description = result['weather'][0]['description'],
                temperature = result['main']['temp'],
                min_temperature = result['main']['temp_min'],
                max_temperature = result['main']['temp_max'],
                pressure = result['main']['pressure'],
                humidity = result['main']['humidity'],
                wind_speed = result['wind']['speed']
            ))
        
        weather_obj = weatherData.objects.all().order_by('-created_at')
        paginator = PageNumberPagination()
        paginator.page_size = 25
        details = paginator.paginate_queryset(weather_obj, request)
        return paginator.get_paginated_response(
            {
                "code": 200,
                "data": WeatherDataSerializer(details, many=True).data
            }
        )
    except Exception as e:
        return Response({"code":300, "message":'Failed', "details":str(e)})
    
    
@api_view(["GET"])
def authenticate_user(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('password')
        if not (username and password):
            return Response({"code":300, "message": "Invalid username or password"})
        user = weatherUser.objects.filter(user_name=username, password=password)
        if user.count():
            return Response({"code":200, "message": "Successfull"})
        else:
            return Response({"code":300, "message": "Invalid username or password"})
    except Exception as e:
        return Response({"code" : 400, "error" : str(e)})


@api_view(["POST"])
def user_create(request):
    try:
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        if not (username and password and email):
            return Response({"code":300, "message": "Please enter all three fields."})
        email_check = weatherUser.objects.filter(email=email) 
        if email_check.count():
            return Response({"code":300, "message": "email already exists"})
        username_check = weatherUser.objects.filter(user_name=username)
        if username_check.count():
            return Response({"code":300, "message": "username already exists"})
        user = weatherUser.objects.create(user_name=username, password=password, email=email)
        return Response({"code":200, "message": "Successfull"})
    except Exception as e:
        return Response({"code" : 400, "error" : str(e)})