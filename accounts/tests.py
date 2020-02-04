from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

# Create your tests here.
class LoginTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='acctest', password='20acctest', email='acctest@somewhere.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_good_login(self):
        user = authenticate(username='acctest', password='20acctest')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='20acctest')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='acctest', password='wr0ng')
        self.assertFalse(user is not None and user.is_authenticated)