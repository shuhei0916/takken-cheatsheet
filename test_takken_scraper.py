import unittest
# from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTakkenScraper(unittest.TestCase):
    # def setUp(self):
    #     pass
    
    def test_get_title(self):
        driver = webdriver.Chrome() 
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')
        title = driver.title
        self.assertEqual(title, "Web form")
        
    def test_question_extraction(self):
        driver = webdriver.Chrome() 
        driver.get('https://www.selenium.dev/selenium/web/web-form.html')
        
        actual = scrape_quetion
        expected = "1"
        self.assertEqual(actual, expected)
        
    
if __name__ == "__main__":
    unittest.main()