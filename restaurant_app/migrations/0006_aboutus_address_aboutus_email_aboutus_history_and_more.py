# Generated by Django 5.1.7 on 2025-04-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant_app", "0005_positionlist_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutus",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="history",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="name",
            field=models.CharField(default="Mono Food", max_length=255),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="opening_hours",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
