'''
TODO: 問題文等は画面をリロードすると内容が毎回変わるので、以下のようなやり方で最小限のテストを実装した。
    - 問題文に「答えよ。」という文字列が含まれているかどうか
    - 選択肢文に、句点（。）が含まれているかどうか
    
    必要なテストケースを全て網羅できているわけではないので注意。
'''

import unittest
import re
from unittest.mock import mock_open, patch, MagicMock
from selenium import webdriver
from selenium.webdriver.common.by import By
from takken_scraper import button_click, scrape_info, scrape_answer, scrape_kaisetsu, scrape_option_text, scrape_question_text, collect_and_write_questions_to_csv


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
    
    def test_scrape_question_text(self):
        question = scrape_question_text(self.driver)
        self.assertIn("答えよ。", question) # おいおい、こんなテストでいいのか笑
    
    def test_option_text(self):
        option_text = scrape_option_text(self.driver)
        self.assertIn("。", option_text) # 句読点が含まれているかどうかのみをテストしている。
    
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
        expected = r"(誤り|正しい|不適当|適当|違反する|違反しない)" # NOTE: 必要なテストケース全てを網羅できているわけではない
        self.assertRegex(kaisetsu, expected)


class TestCSVWriter(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {
                "year": "令和3年",
                "question_number": "問1",
                "option_number": "肢1",
                "question_text": "次の文は…",
                "option_text": "1. 選択肢1",
                "answer": "正",
                "kaisetsu": "この解説は…"
            }
        ]
        
    @patch('builtins.open', new_callable=mock_open)
    def test_csv_header(self, mock_file):
        # ダミーのドライバを使ってテスト
        driver = None
        
        collect_and_write_questions_to_csv(driver, num_questions=1, filename="dummy.csv")

        # 書き込まれた内容を確認
        mock_file.assert_called_once_with('dummy.csv', mode='w', newline='', encoding='utf-8')
        handle = mock_file()
        handle.write.assert_any_call("year,question_number,option_number,question_text,option_text,answer,kaisetsu\n")


if __name__ == "__main__":
    unittest.main()