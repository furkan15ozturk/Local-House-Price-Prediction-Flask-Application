from unittest import TestCase
import pandas as pd
from location_to_lat_long import location_to_lat_long
import os

class Test(TestCase):
    def test_location_to_lat_long(self):
        # Mock CSV file data
        csv_data = "CSV Files/test_adalar.csv"

        # Create a temporary CSV file for testing
        with open("test.csv", "w") as f:
            f.write(csv_data)

        # Call the function being tested
        result_df = location_to_lat_long()

        # Perform assertions on the result
        self.assertIsInstance(result_df, pd.DataFrame)

        # Load the prepared CSV file for comparison
        prepared_df = pd.read_csv("test.csv")

        # Check if the "lat" and "lng" columns match the prepared CSV file
        for index, row in result_df.iterrows():
            lat = row['lat']
            lng = row['lng']
            if index < len(prepared_df):
                # Get the corresponding row in the prepared DataFrame
                prepared_row = prepared_df.iloc[index]

                # Compare lat and lng values
                self.assertEqual(lat, prepared_row['lat'])
                self.assertEqual(lng, prepared_row['lng'])

        # Clean up the temporary CSV file
        os.remove("test.csv")

