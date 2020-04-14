from django.test import TestCase
from app.numbercalc import add_number, subtract_number


class AddTest(TestCase):

    def test_add_number(self):
        """this function will test the add_number function
        and will add 2 numbers"""
        self.assertEqual(add_number(5, 5), 10)

    def test_subtract_number(self):
        """this function will test the subtract function
        and will subtract one number from another"""
        self.assertEqual(subtract_number(8, 5), 3)
