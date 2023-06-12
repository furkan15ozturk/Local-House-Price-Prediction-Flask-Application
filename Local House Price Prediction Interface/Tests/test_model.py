from unittest import TestCase
from model import prediction, preprocessor
import numpy as np

class Test(TestCase):
    def test_prediction(self):
        # Test case inputs
        area = 150
        absolute_area = 140
        room = 3
        floor_count = 5
        building_age = 0
        lat = 40.1234
        lng = 29.5678

        # Call the function being tested
        result = prediction(area, absolute_area, room, floor_count, building_age, lat, lng, 4)

        # Perform assertions on the result
        self.assertIsInstance(result, str)

    def test_preprocessor(self):
        # Test case inputs
        X = np.array([[150, 140, 3, 5, 40.1234, 29.5678, 10, 50, 0, 1, 0, 0, 0],
                      [200, 180, 4, 4, 39.5548, 30.4587, 20, 50, 0, 0, 1, 0, 0]])

        # Call the function being tested
        result = preprocessor(X)

        # Perform assertions on the result
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, X.shape)
