import unittest
import re
# from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from takken_scraper import scrape_question, button_click, scrape_info, scrape_answer, scrape_kaisetsu


class TestTakkenScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # クラス全体で一回だけwebdriverを初期化(setupメソッドは各テストメソッドの前に呼ばれる)
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://takken-siken.com/marubatu.php')
        
        button_click(cls.driver)
        
    @classmethod
    def tearDownClass(cls):
        # 全テスト後にwebdriverを終了
        cls.driver.quit()        
    
    # def test_scrape_question(self):
    #     question = scrape_question(self.driver)
    #     self.assertIn("答えよ。", question) # おいおい、こんなテストでいいのか笑
    
    def test_scraper_year(self):
        year, _, _ = scrape_info(self.driver)
        expected = r"(平成|令和)" # NOTE: 平成と令和という文字列が含まれていることのみを確認
        self.assertRegex(year, expected)
        
    def test_scrape_ques_num(self):
        _, ques_num, _ = scrape_info(self.driver)
        expected = r"問\d+"
        self.assertRegex(ques_num, expected)
        
    def test_scrape_ques_num(self):
        _, _, opt_num = scrape_info(self.driver)
        expected = r"肢\d+"
        self.assertRegex(opt_num, expected)
        
    def test_scrape_answer(self):
        answer = scrape_answer(self.driver)
        expected = r"(正|誤)"
        self.assertRegex(answer, expected)
        
    def test_scrape_kaisetsu(self):
        kaisetsu = scrape_kaisetsu(self.driver)
        expected = r"(誤り。|正しい。|不適当。|適当。)"
        self.assertRegex(kaisetsu, expected)
        
    
        
        
if __name__ == "__main__":
    unittest.main()