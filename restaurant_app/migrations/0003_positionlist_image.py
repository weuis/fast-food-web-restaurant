# Generated by Django 5.1.6 on 2025-04-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant_app", "0002_alter_positionlist_chef"),
    ]

    operations = [
        migrations.AddField(
            model_name="positionlist",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="menu_images/"),
        ),
    ]
