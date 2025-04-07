from django.urls import path
from restaurant_app.views import (
    HomeView,
    BookTableView,
    FeedbackView,
    AboutView,
    MenuView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('book_table/', BookTableView.as_view(), name='book_table'),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
]

app_name = "restaurant_app"
