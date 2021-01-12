from django.test import TestCase
from django.core.exceptions import ValidationError
from products.models import Product
from .models import Order, OrderLineItem
# Create your tests here.
class OrderTests(TestCase):
    """To test validation of the Order model """
    def setUp(self):
        self.order = Order(username="TestUser", full_name = "Test User", phone_number = "0871234567", country = "Ireland",postcode = "D1", town_or_city = "Dublin",street_address1 = "123 Street", street_address2 = "Rathgar", county = "Dublin", date = "2020-02-04")
        self.order.save()
        self.product = Product(name="TestProduct", description="TestProduct description", price="100.99", image="images/test.jpg", rating="0.0")
        self.product.save()
        self.order_line_item = OrderLineItem(order=self.order, product=self.product, quantity = "0")
        self.order_line_item.save()

    def tearDown(self):
        self.order_line_item.delete()
        self.order.delete()
        self.product.delete()

    def test_str(self):
        self.assertEqual(self.order.full_name, 'Test User')
        self.assertEqual(self.order.date, '2020-02-04')
        self.assertEqual(self.order_line_item.product, self.product)
        self.assertEqual(self.order_line_item.quantity, '0')

    def test_username_blank(self):
        self.order.username = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_username_max(self):
        self.order.username = 'abcdefghijklmnopqrstu'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 20 characters"):     
            self.order.full_clean()

    def test_fullname_blank(self):
        self.order.full_name = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_fullname_max(self):
        self.order.full_name = 'abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyz'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 50 characters"):     
            self.order.full_clean()

    def test_phone_blank(self):
        self.order.phone_number = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_phone_max(self):
        self.order.phone_number = '123456789012345678901'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 20 characters"):     
            self.order.full_clean()

    def test_country_blank(self):
        self.order.country = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_country_max(self):
        self.order.country = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmno'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 40 characters"):     
            self.order.full_clean()

    #Postcode can be blank
    def test_postcode_blank(self):
        self.order.postcode = ''
        self.assertEqual(self.order.postcode, '')

    def test_postcode_max(self):
        self.order.postcode = 'abcdefghijklmnopqrstu'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 20 characters"):     
            self.order.full_clean()

    def test_town_or_city_blank(self):
        self.order.town_or_city = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_town_or_city_max(self):
        self.order.town_or_city = 'abcdefghijklmnopqrstuvwxyabcdefghijklmnop'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 40 characters"):     
            self.order.full_clean()

    def test_street_address1_blank(self):
        self.order.street_address1 = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_street_address1_max(self):
        self.order.street_address1 = 'abcdefghijklmnopqrstuvwxyabcdefghijklmnop'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 40 characters"):     
            self.order.full_clean()

    def test_street_address2_blank(self):
        self.order.street_address2 = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_street_address2_max(self):
        self.order.street_address2 = 'abcdefghijklmnopqrstuvwxyabcdefghijklmnop'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 40 characters"):     
            self.order.full_clean()

    def test_county_blank(self):
        self.order.county = ''
        with self.assertRaisesRegexp(ValidationError, "This field cannot be blank."):     
            self.order.full_clean()

    def test_county_max(self):
        self.order.county = 'abcdefghijklmnopqrstuvwxyabcdefghijklmnop'
        with self.assertRaisesRegexp(ValidationError, "Ensure this value has at most 40 characters"):     
            self.order.full_clean()

    def test_order_quantity_blank(self):
        self.order_line_item.quantity = ''
        with self.assertRaisesRegexp(ValidationError, "value must be an integer."):     
            self.order_line_item.full_clean()
       

    def test_order_product_blank(self):
        with self.assertRaises(ValueError):
             self.order_line_item.product = ''  
            

    
