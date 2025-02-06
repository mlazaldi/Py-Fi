#%%
import unittest
from flask import Flask
from views import views  # Replace 'your_app' with the name of your Flask app module

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.views = views.test_client()  # Create a test client for the app

    def test_data_returned(self):
        response = self.views.get('/data')  # Replace '/your_route' with the actual route
        self.assertEqual(response.status_code, 200)

        # Check if the response data is as expected
        expected_data = {'key': 'value'}  # Replace with your expected data
        self.assertEqual(response.get_json(), expected_data)

if __name__ == '__main__':
    unittest.main()