from unittest import TestCase
from app import get_lat_long
from flask import Flask, render_template

class Test(TestCase):

    def test_get_lat_long(self):
        # Test case input
        address = "Istanbul Buyukcekmece Tepecik Mahallesi"

        # Call the function being tested
        result = get_lat_long(address)

        # Perform assertions on the result
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], float)
        self.assertIsInstance(result[1], float)

    def test_app(self):
        app = Flask(__name__)
