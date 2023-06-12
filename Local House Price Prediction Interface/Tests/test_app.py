from unittest import TestCase
from app import get_lat_long
from flask import Flask, render_template
from app import app

class Test(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        app.config['WTF_CSRF_ENABLED'] = False

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

    def test_contact(self):
        with self.app as client:
            response = client.get('/contact')
            self.assertEqual(response.status_code, 200)

    def test_about(self):
        with self.app as client:
            response = client.get('/about')
            self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        with self.app as client:
            data = {
                'area': '220',
                'absolute_area': '200',
                'room': '3',
                'floor_count': '5',
                'building_age': '0',
                'location': 'İstanbul Buyukcekmece Tepecik Mahallesi',
                'model': '4'
            }

            response = client.post('/', data=data)
            self.assertEqual(response.status_code, 200)