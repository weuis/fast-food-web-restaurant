from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Position, PositionList, AboutUs, BookTable, Feedback
from django import forms


def about_view(request: HttpRequest) -> HttpResponse:
    restaurant = AboutUs.objects.first()
    context = {"restaurant": restaurant}
    return render(request, "restaurant_app/about.html", context=context)


def menu_view(request: HttpRequest) -> HttpResponse:
    positions = Position.objects.all()
    menu_items = PositionList.objects.all()

    context = {
        "positions": positions,
        "menu_items": menu_items,
    }

    return render(request, "restaurant_app/menu.html", context=context)


def book_table_view(request: HttpRequest) -> HttpResponse:
    context = {}

    if request.method == "POST":
        name = request.POST.get("user_name", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        if phone_number.isdigit():
            phone_number = int(phone_number)
        email = request.POST.get("user_email", "").strip()
        total_person = request.POST.get("total_person", "").strip()
        booking_data = request.POST.get("booking_data", "").strip()
        try:
            total_person = int(total_person)
        except ValueError:
            total_person = 0

        if total_person > 0 and booking_data:
            data = BookTable(
                name=name,
                phone_number=phone_number,
                email=email,
                total_person=total_person,
                booking_date=booking_data,
            )
            data.save()
            context["message"] = "Booking successful!"
        else:
            context["error"] = "Invalid input. Please check your details."
        context.update(
            {
                "user_name": name,
                "phone_number": phone_number,
                "user_email": email,
                "total_person": total_person,
                "booking_data": booking_data,
            }
        )

    return render(request, "restaurant_app/book_table.html", context=context)


class HomeView(ListView):
    template_name = "restaurant_app/home.html"
    context_object_name = "position_list"
    model = PositionList

    def get_queryset(self):
        category_id = self.request.GET.get("category_id")
        sort_order = self.request.GET.get("sort", "asc")

        queryset = PositionList.objects.all()
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset.order_by("-price" if sort_order == "desc" else "price")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "positions": Position.objects.all().order_by("position_name"),
                "reviews": Feedback.objects.all().order_by("-id")[:5],
                "selected_category": self.request.GET.get("category_id"),
                "selected_sort": self.request.GET.get("sort", "asc"),
            }
        )
        return context


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["user_name", "description", "rating"]

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if not (1 <= rating <= 5):
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "restaurant_app/feedback.html"
    success_url = reverse_lazy("restaurant_app:feedback")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feedback_list"] = Feedback.objects.all().order_by("-id")
        return context
