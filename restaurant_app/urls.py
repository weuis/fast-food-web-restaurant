from django.urls import path

from restaurant_app.views import home

urlpatterns = [
    path("", home, name="home"),
]