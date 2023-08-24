import unittest
from ticket_websites import get_company_info

class TestGetCompanyInfo(unittest.TestCase):
    def test_valid_company(self):
        company_url = "https://www.consumeraffairs.com/entertainment/seatgeek.html"
        company_name, company_rating = get_company_info(company_url)
        self.assertEqual(company_name, "Example Company")
        self.assertEqual(company_rating, "4.0")

if __name__ == "__main__":
    unittest.main()