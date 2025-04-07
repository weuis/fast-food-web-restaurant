from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from .models import Position, PositionList, AboutUs, BookTable, Feedback
from django import forms


class AboutView(TemplateView):
    template_name = "restaurant_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["restaurant"] = AboutUs.objects.first()
        return context


class MenuView(TemplateView):
    template_name = "restaurant_app/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "positions": Position.objects.all(),
            "menu_items": PositionList.objects.all(),
        })
        return context


class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ["name", "phone_number", "email", "total_person", "booking_date"]


class BookTableView(FormView):
    template_name = "restaurant_app/book_table.html"
    form_class = BookTableForm
    success_url = reverse_lazy("restaurant_app:book_table")

    def form_valid(self, form):
        form.save()
        context = self.get_context_data(form=form)
        context["message"] = "Booking successful!"
        return self.render_to_response(context)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context["error"] = "Invalid input. Please check your details."
        return self.render_to_response(context)


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
        context.update({
            "positions": Position.objects.all().order_by("position_name"),
            "reviews": Feedback.objects.all().order_by("-id")[:5],
            "selected_category": self.request.GET.get("category_id"),
            "selected_sort": self.request.GET.get("sort", "asc"),
        })
        return context


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["user_name", "feedback", "rating"]

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