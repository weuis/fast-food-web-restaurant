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

def home_view(request: HttpRequest) -> HttpResponse:
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

def about_view(request: HttpRequest) -> HttpResponse:
    data = AboutUs.objects.all()
    context = {
        'data': data
    }
    return render(request, 'restaurant_app/about.html', context=context)


def menu_view(request: HttpRequest) -> HttpResponse:
    positions = Position.objects.all()
    menu_items = PositionList.objects.all()

    context = {
        'positions': positions,
        'menu_items': menu_items,
    }

    return render(request, 'restaurant_app/menu.html', context=context)

def book_table_view(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == 'POST':
        name = request.POST.get('user_name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        email = request.POST.get('user_email', '').strip()
        total_person = request.POST.get('total_person', '').strip()
        booking_data = request.POST.get('booking_data', '').strip()
        try:
            total_person = int(total_person)
        except ValueError:
            total_person = 0

        if name and len(phone_number) == 10 and email and total_person > 0 and booking_data:
            data = BookTable(Name=name, Phone_number=phone_number,
                             Email=email, Total_person=total_person,
                             Booking_date=booking_data)
            data.save()
            context['message'] = "Booking successful!"
        else:
            context['error'] = "Invalid input. Please check your details."
        context.update({
            'user_name': name,
            'phone_number': phone_number,
            'user_email': email,
            'total_person': total_person,
            'booking_data': booking_data,
        })

    return render(request, 'restaurant_app/book_table.html', context=context)
