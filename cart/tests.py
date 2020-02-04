from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from datetime import datetime
from products.models import Product
from .models import Cart, CartItem

# Create your tests here.
class CartTests(TestCase):
    """To test validation of the Cart model """
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='acctest', password='20acctest', email='acctest@somewhere.com')
        self.user.save()
        self.cart = Cart(id = '1', user = self.user, created = datetime.now)
        self.product = Product(name="TestProduct", description="TestProduct description", price="100.99", image="images/test.jpg", rating="0.0")
        self.product.save()
        self.cart_item = CartItem(id = '1', cart = self.cart, product = self.product, quantity = '1')

    def tearDown(self):
        self.product.delete()
        self.cart_item.delete()
        self.cart.delete()
        self.user.delete()
        

    def test_str(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(self.cart_item.cart, self.cart)

    def test_cart_item_quantity_blank(self):
        self.cart_item.quantity = ''
        with self.assertRaisesRegexp(ValidationError, "value must be an integer."):     
            self.cart_item.full_clean()
       

    def test_cart_item_product_blank(self):
        with self.assertRaises(ValueError):
             self.cart_item.product = ''
        