import unittest
from hotel_reviews import hotel_info

class HotelReviewsTests(unittest.TestCase):
    def test_hotel_info(self):
        self.assertIsNotNone(hotel_info("Westin"))

