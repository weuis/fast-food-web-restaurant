from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse

from .models import (
    Position,
    PositionList,
    Chef,
    AboutUs,
    BookTable,
    Feedback
)

def home_view(request: HttpRequest) -> HttpResponse:
    positions = Position.objects.all().order_by('position_name')

    reviews = Feedback.objects.all().order_by('-id')[:5]

    category_id = request.GET.get('category_id')
    sort_order = request.GET.get('sort', 'asc')

    if category_id:
        position_list = PositionList.objects.filter(category_id=category_id)
    else:
        position_list = PositionList.objects.all()

    if sort_order == 'desc':
        position_list = position_list.order_by('-price')
    else:
        position_list = position_list.order_by('price')

    context = {
        'positions': positions,
        'position_list': position_list,
        'reviews': reviews,
        'selected_category': category_id,
        'selected_sort': sort_order
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
        if phone_number.isdigit():
            phone_number = int(phone_number)
        email = request.POST.get('user_email', '').strip()
        total_person = request.POST.get('total_person', '').strip()
        booking_data = request.POST.get('booking_data', '').strip()
        try:
            total_person = int(total_person)
        except ValueError:
            total_person = 0

        if total_person > 0 and booking_data:
            data = BookTable(name=name, phone_number=phone_number,
                             email=email, total_person=total_person,
                             booking_date=booking_data)
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

def feedback_view(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == 'POST':
        user_name = request.POST.get('user_name', '').strip()
        description = request.POST.get('description', '').strip()
        rating = request.POST.get('rating', '').strip()

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError("Invalid rating")
        except ValueError:
            rating = None

        if user_name and description and rating is not None:
            Feedback.objects.create(user_name=user_name, description=description, rating=rating)
            context['message'] = "Thank you for your feedback!"
            return redirect('restaurant_app:feedback')
        else:
            context['error'] = "Please fill out all fields correctly."

        context.update({
            'user_name': user_name,
            'description': description,
            'rating': rating
        })
    context['feedback_list'] = Feedback.objects.all().order_by('-id')
    return render(request, 'restaurant_app/feedback.html', context=context)
