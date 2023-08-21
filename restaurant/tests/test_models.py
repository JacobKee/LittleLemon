from ..models import Menu
from django.test import TestCase

# TestCase class


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            name="IceCream", price=80, menu_item_description="Dessert")
        self.assertEqual(item, "IceCream : 80")
