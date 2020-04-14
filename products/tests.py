from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    here we'll define the Tests that we'll run against out Post models
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
