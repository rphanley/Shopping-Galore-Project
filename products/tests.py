from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Product


# Create your tests here.
class ProductTests(TestCase):
    """To test validation of the Product model """

    def setUp(self):
        self.product = Product(name="TestProduct", description="TestProduct description", price="100.99", image="images/test.jpg", rating="0.0")
        self.product.save()

    def tearDown(self):
        self.product.delete()

    def test_str(self):
        self.assertEqual(self.product.name, 'TestProduct')

    def test_str_max(self):
        self.product.name = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 254 characters"):     
            self.product.full_clean()

    def test_rating_min(self):
        self.product.rating = '-0.1'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value is greater than or equal to 0."):     
            self.product.full_clean()

    def test_rating_max(self):
        self.product.rating = '5.1'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value is less than or equal to 5."):     
            self.product.full_clean()

    def test_price(self):
        self.product.price = '101.99'
        self.product.save()
        self.assertEqual(self.product.price, '101.99')

    def test_price_dp(self):
        self.product.price = '1000.999'
        with self.assertRaisesRegexp(ValidationError, "Ensure that there are no more than 2 decimal places."):     
            self.product.full_clean()

    def test_price_maxdigits(self):
        self.product.price = '1000000.99'
        with self.assertRaisesRegexp(ValidationError, "Ensure that there are no more than 8 digits in total."):     
            self.product.full_clean()

