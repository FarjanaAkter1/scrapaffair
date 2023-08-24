import unittest
from unittest.mock import Mock, patch
from scrape_travel_sites import extract_reviews

class TestScrapeTravelSites(unittest.TestCase):
    @patch('scrape_travel_sites.requests.get')
    @patch('scrape_travel_sites.BeautifulSoup')
    def test_extract_reviews(self, mock_bs, mock_get):
        # Prepare mock response
        mock_response = Mock()
        mock_response.content = """
            <span class="last-word-wrapper">Mock Company</span>
            <div class="rvw__top-text">Mock review 1</div>
            <meta itemprop="ratingValue" content="4">
        """
        mock_get.return_value = mock_response

        # Call the function to test
        result = extract_reviews("mock-company")

        # Assertions
        expected_result = [("Mock Company", 4, "Mock review 1")]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()