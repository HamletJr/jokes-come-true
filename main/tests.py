from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        item = Product.objects.create(
            name= "Self-Modeling Resin",
            price = 1200,
            description = "Rare material used to custom-make Relics. It can model itself according to expectations.",
            quantity = 1,
        )
        self.assertTrue(item.is_product_available)