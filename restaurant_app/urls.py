from django.urls import path
from restaurant_app.views import (
    HomeView,
    book_table_view,
    FeedbackView,
    about_view,
    menu_view,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", about_view, name="about"),
    path("menu/", menu_view, name="menu"),
    path("book-table/", book_table_view, name="book_table"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
]

app_name = "restaurant_app"
