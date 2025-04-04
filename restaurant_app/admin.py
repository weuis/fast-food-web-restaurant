from django.contrib import admin
from .models import Position, PositionList, Chef, AboutUs, Feedback, BookTable


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "position_name")
    search_fields = ("position_name",)


@admin.register(PositionList)
class PositionListAdmin(admin.ModelAdmin):
    list_display = ("id", "position_name", "price", "category", "chef", "image")
    search_fields = ("position_name", "category__position_name", "chef__username")
    list_filter = ("category", "chef")


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_chef", "email")
    search_fields = ("username", "email")
    list_filter = ("is_chef",)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "opening_hours", "address")
    search_fields = ("name", "address", "phone", "email", "history", "description")
    list_filter = ("opening_hours",)
    ordering = ("name",)
    readonly_fields = ("name",)
    fieldsets = (
        ("General Info", {"fields": ("name", "description", "history")}),
        ("Contact Details", {"fields": ("address", "phone", "email")}),
        ("Working Hours", {"fields": ("opening_hours",)}),
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "rating")
    search_fields = ("user_name",)
    list_filter = ("rating",)


@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone_number",
        "email",
        "total_person",
        "booking_date",
    )
    search_fields = ("name", "email", "phone_number")
    list_filter = ("booking_date", "total_person")
