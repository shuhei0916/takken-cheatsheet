import unittest
import re
# from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from takken_scraper import scrape_question, button_click, scrape_year


class TestTakkenScraper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get('https://takken-siken.com/marubatu.php')
        
        button_click(self.driver)

    # def test_get_title(self):
    #     title = self.driver.title
    #     self.assertEqual(title, "宅建士 一問一答道場🥋｜宅建試験ドットコム")
        
    # def test_question_extraction(self):        
    #     question = scrape_question(self.driver)
    #     expected = "制限行為能力者に関する次の記述のうち、民法の規定によれば、正しいか否かを答えよ。"
    #     self.assertEqual(question, expected)
    
    # def test_scrape_question(self):
    #     question = scrape_question(self.driver)
    #     self.assertIn("答えよ。", question) # おいおい、こんなテストでいいのか笑
    
    def test_scraper_year(self):
        year = scrape_year(self.driver)
        expected = r"(平成|令和)\d+年試験" # NOTE: 平成と令和のみ対応
        self.assertRegex(year, expected)
        
    # def test_scrape_opt_num(self):
    #      問\d+ 肢\d+
        
    
if __name__ == "__main__":
    unittest.main()