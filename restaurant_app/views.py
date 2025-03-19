from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .models import (
    Position,
    PositionList,
    Feedback,
    Chef,
    AboutUs,
    BookTable,
    Feedback
)

def home(request: HttpRequest) -> HttpResponse:
    positions = Position.objects.all()
    position_list = PositionList.objects.all()
    review = Feedback.objects.all()

    context = {
        'positions': positions,
        'position_list': position_list,
        'review': review
    }
    return render(
        request,
        'restaurant_app/home.html',
        context=context
    )

def about(request: HttpRequest) -> HttpResponse:
    data = AboutUs.objects.all()
    context = {
        'data': data
    }
    return render(request, 'restaurant_app/about.html', context=context)


def menu(request):
    positions = Position.objects.all()
    menu_items = PositionList.objects.all()

    context = {
        'positions': positions,
        'menu_items': menu_items,
    }

    return render(request, 'restaurant_app/menu.html', context)

