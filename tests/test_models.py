from django.test import TestCase
from django.utils import timezone

from restaurant_app.models import(
    Position,
    PositionList,
    Chef,
    AboutUs,
    Feedback,
    BookTable,
)


class ModelTests(TestCase):
    def setUp(self):
        self.chef = Chef.objects.create_user(username="alex", password="pass123", is_chef=True)
        self.position_category = Position.objects.create(position_name="Pizza")
        self.position = PositionList.objects.create(
            position_name="Margherita",
            description="Tomato, mozzarella, basil",
            price=1000,
            category=self.position_category,
            chef=self.chef
        )

    def test_position_str(self):
        self.assertEqual(str(self.position_category), "Pizza")

    def test_positionlist_creation(self):
        self.assertEqual(str(self.position), "Margherita")
        self.assertEqual(self.position.price, 1000)
        self.assertEqual(self.position.chef.username, "alex")
        self.assertEqual(self.position.category.position_name, "Pizza")

    def test_chef_str(self):
        self.assertEqual(str(self.chef), "alex")
        self.assertTrue(self.chef.is_chef)

    def test_about_us_str(self):
        about = AboutUs.objects.create(
            description="Welcome to Mono Food!",
            address="Main Street 123"
        )
        self.assertEqual(str(about), "Mono Food")

    def test_feedback_str(self):
        feedback = Feedback.objects.create(
            user_name="Jason",
            feedback="Perfect place!",
            rating=5
        )
        self.assertEqual(str(feedback), "Jason")
        self.assertEqual(feedback.rating, 5)

    def test_book_table_str(self):
        booking = BookTable.objects.create(
            name="Alex",
            phone_number=1234567890,
            email="alex@outlook.com",
            total_person=2,
            booking_date=timezone.now().date()
        )
        self.assertEqual(str(booking), "Alex")
        self.assertEqual(booking.total_person, 2)
