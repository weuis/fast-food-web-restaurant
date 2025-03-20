from django.urls import path

from restaurant_app.views import home_view, about_view, menu_view, book_table_view
urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),

    path("menu/", menu_view, name="menu"),

    path("book-table/", book_table_view, name="book_table" ),


]

app_name= "restaurant_app"