from django.conf.urls import url, include
from cityweather.views import get_weather,authenticate_user,user_create

urlpatterns = [
    url(r"^authenticate-user/$", authenticate_user, name="matching-listing"),
    url(r"^user-create/$", user_create, name="applied-rider"),
    url(r"^get-weather/$", get_weather, name="get-rider"),
]