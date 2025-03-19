from django.urls import path

from restaurant_app.views import home, about, menu
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),

    path("menu/", menu, name="menu"),


]

app_name= "restaurant_app"