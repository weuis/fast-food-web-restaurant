from django.test import TestCase
from django.urls import reverse
from restaurant_app.models import AboutUs, BookTable, Feedback, Position, PositionList
from django.contrib.auth import get_user_model


class AboutViewTests(TestCase):
    def setUp(self):
        AboutUs.objects.create(
            name="Mono Food",
            description="A great place to eat!",
            history="We started in 2020.",
        )

    def test_about_view(self):
        """Test if the about view loads correctly and uses the correct template."""
        url = reverse('restaurant_app:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_app/about.html')
        self.assertContains(response, "Mono Food")


class MenuViewTests(TestCase):
    def test_menu_view(self):
        """Test if the menu view works and uses the correct template."""
        url = reverse('restaurant_app:menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_app/menu.html')


class BookTableViewTests(TestCase):
    def test_book_table_post_success(self):
        """Test if the book table view handles valid POST request correctly."""
        url = reverse('restaurant_app:book_table')
        response = self.client.post(url, {
            'user_name': 'John Doe',
            'phone_number': '1234567890',
            'user_email': 'john@example.com',
            'total_person': 3,
            'booking_data': '2025-04-10'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Booking successful!")

    def test_book_table_post_error(self):
        """Test if the book table view handles invalid POST request correctly."""
        url = reverse('restaurant_app:book_table')
        response = self.client.post(url, {
            'user_name': 'John Doe',
            'phone_number': 'abc',
            'user_email': 'john@example.com',
            'total_person': 0,
            'booking_data': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid input. Please check your details.")


class HomeViewTests(TestCase):
    def test_home_view(self):
        """Test if HomeView renders and returns correct context."""
        url = reverse('restaurant_app:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_app/home.html')
        self.assertIn('position_list', response.context)


class FeedbackViewTests(TestCase):
    def test_feedback_get(self):
        """Test if Feedback view renders correctly on GET request."""
        url = reverse('restaurant_app:feedback')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_app/feedback.html')

    def test_feedback_post_success(self):
        """Test if feedback form works correctly on valid POST request."""
        url = reverse('restaurant_app:feedback')
        response = self.client.post(url, {
            'user_name': 'John Doe',
            'feedback': 'Great service!',
            'rating': 5
        })
        self.assertRedirects(response, reverse('restaurant_app:feedback'))
        self.assertEqual(Feedback.objects.count(), 1)

