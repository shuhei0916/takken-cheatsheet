import unittest
# from unittest.mock import MagicMock
from takken_scraper import scrape_question, scrape_year
from bs4 import BeautifulSoup


class TestTakkenScraper(unittest.TestCase):
    def setUp(self):
        # テスト用のHTMLファイルを読み込む
        with open('sample.html', 'r', encoding='utf-8') as f:
            self.html_content = f.read() 
        self.soup = BeautifulSoup(self.html_content, 'html.parser')
            
        
    def test_question_extraction(self):
        question, _ = scrape_question(self.soup)
        expected_question = "相隣関係に関する次の記述のうち、民法の規定によれば、正しいものはどれか。"
        self.assertEqual(question, expected_question)

    def test_number_extraction(self):
        _, number = scrape_question(self.soup)
        expected_number = "2"
        self.assertEqual(number, expected_number)
        
    def test_year_extraction(self):
        actual = scrape_year(self.soup)
        expected = "令和5年"
        self.assertEqual(actual, expected)
        
    
if __name__ == "__main__":
    unittest.main()