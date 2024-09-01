import unittest
# from unittest.mock import MagicMock
from takken_scraper import scrape_question
from bs4 import BeautifulSoup


class TestTakkenScraper(unittest.TestCase):
    def setUp(self):
        # テスト用のHTMLファイルを読み込む
        with open('sample.html', 'r', encoding='utf-8') as f:
            self.html_content = f.read()
        
    def test_question_extraction(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        question, _ = scrape_question(soup)
        
        expected_question = "次の1から4までの記述のうち、民法の規定、判例及び下記判決文によれば、誤っているものはどれか。"
        self.assertEqual(question, expected_question)

    def test_number_extraction(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        _, number = scrape_question(soup)
        
        expected_number = "1"
        self.assertEqual(number, expected_number)
        
    
if __name__ == "__main__":
    unittest.main()