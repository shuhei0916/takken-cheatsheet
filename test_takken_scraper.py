import unittest
# from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from takken_scraper import scrape_question


class TestTakkenScraper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get('https://takken-siken.com/marubatu.php')

    # def test_get_title(self):
    #     title = self.driver.title
    #     self.assertEqual(title, "宅建士 一問一答道場🥋｜宅建試験ドットコム")
        
    def test_question_extraction(self):        
        question = scrape_question(self.driver)
        expected = "制限行為能力者に関する次の記述のうち、民法の規定によれば、正しいか否かを答えよ。"
        self.assertEqual(question, expected)
        
    
if __name__ == "__main__":
    unittest.main()