from django.test import TestCase
from django.core.exceptions import ValidationError
from products.models import Product
from .models import Feedback

# Create your tests here.
class FeedbackTests(TestCase):
    """To test validation of the Feedback model """

    def setUp(self):
        self.product = Product(name="TestProduct", description="TestProduct description", price="100.99", image="images/test.jpg", rating="0.0")
        self.product.save()
        self.feedback = Feedback(product= self.product, user_name="TestUser", email="test@somewhere.com", content="Test Content", rating="0.0", date="2020-02-04")
        self.feedback.save()

    def tearDown(self):
        self.product.delete()
        self.feedback.delete()

    def test_str(self):
        self.assertEqual(self.product.name, 'TestProduct')

    def test_user_name(self):
        self.assertEqual(self.feedback.user_name, 'TestUser')

    def test_user_name_max(self):
        self.feedback.user_name = 'abcdefghijklmnopqrstuvwxyzabcdabcdefghijklmnopqrstuvwxyzabcdabcdefghijklmnopqrstuvwxyzabcdabcdefghijklmnopqrstuvwxyzabcde'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 120 characters"):     
            self.feedback.full_clean()

    def test_rating_min(self):
        self.feedback.rating = '-0.1'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value is greater than or equal to 0."):     
            self.feedback.full_clean()

    def test_rating_max(self):
        self.feedback.rating = '5.1'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value is less than or equal to 5."):     
            self.feedback.full_clean()

   