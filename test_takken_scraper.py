import unittest
# from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from takken_scraper import scrape_question


class TestTakkenScraper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get('https://www.selenium.dev/selenium/web/web-form.html')

    
    def test_get_title(self):
        title = self.driver.title
        self.assertEqual(title, "Web form")
        
    def test_question_extraction(self):        
        actual = scrape_question()
        expected = "1"
        self.assertEqual(actual, expected)
        
    
if __name__ == "__main__":
    unittest.main()