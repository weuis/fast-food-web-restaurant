from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.contrib import admin
from restaurant_app.models import PositionList, Position


class AdminCustomConfigTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='123456789'
        )
        self.client.force_login(self.admin_user)

        self.position_category = Position.objects.create(position_name="Pizza")
        self.position = PositionList.objects.create(
            position_name="Margherita",
            description="Tomato, mozzarella, basil",
            price=1000,
            category=self.position_category,
        )

    def test_position_list_registered(self):
        """Check if PositionList is registered in the admin panel"""
        self.assertIn(PositionList, admin.site._registry)

    def test_position_list_admin_config(self):
        """Check if the correct fields are in admin for PositionList"""
        position_list_admin = admin.site._registry[PositionList]
        self.assertEqual(position_list_admin.list_display, (
            "id", "position_name", "price", "category", "chef", "image")
        )
        self.assertEqual(position_list_admin.search_fields, (
            "position_name", "category__position_name", "chef__username")
        )

