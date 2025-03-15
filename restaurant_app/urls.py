from django.urls import path

from restaurant_app.views import home, about
urlpatterns = [
    path("", home, name="index"),
    path("about/", about, name="about"),
]

app_name= "restaurant_app"