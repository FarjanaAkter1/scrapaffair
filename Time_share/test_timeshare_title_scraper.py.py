import unittest
from timeshare_title_scraper import scrape_timeshare_titles

class TestTimeshareTitleScraper(unittest.TestCase):
    def test_scrape_timeshare_titles(self):
        # a real URL for testing
        test_url = "https://www.consumeraffairs.com/travel/timeshares.html" 
        titles = scrape_timeshare_titles(test_url)
        self.assertIsInstance(titles, list)
        self.assertTrue(len(titles) > 0)
        

if __name__ == "__main__":
    unittest.main()
