from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
    position_name = models.CharField(max_length=15)

    def __str__(self):
        return self.position_name


class PositionList(models.Model):
    position_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    category = models.ForeignKey(
        Position,
        related_name="name",
        on_delete=models.CASCADE
    )
    chef = models.ForeignKey(
        "Chef",
        related_name="positions",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.position_name


class Chef(AbstractUser):
    is_chef = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class AboutUs(models.Model):
    description = models.TextField(blank=False)


class Feedback(models.Model):
    user_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.user_name


class BookTable(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.IntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name
