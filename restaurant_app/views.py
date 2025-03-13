from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .models import Position, PositionList, Feedback

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

