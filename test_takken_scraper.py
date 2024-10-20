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
import takken_scraper as ts


class TestTakkenScraper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # クラス全体で一回だけwebdriverを初期化(setupメソッドは各テストメソッドの前に呼ばれる)
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://takken-siken.com/marubatu.php')
        
        ts.click_start_button(cls.driver)
        
    @classmethod
    def tearDownClass(cls):
        # 全テスト後にwebdriverを終了
        cls.driver.quit()        
    
    def test_scrape_question_text(self):
        question = ts.scrape_question_text(self.driver)
        self.assertIn("答えよ。", question) # おいおい、こんなテストでいいのか笑
    
    def test_option_text(self):
        option_text = ts.scrape_option_text(self.driver)
        self.assertIn("。", option_text) # 句読点が含まれているかどうかのみをテストしている。
    
    def test_scraper_year(self):
        year, _, _ = ts.scrape_question_info(self.driver)
        expected = r"(平成|令和)" # NOTE: 平成と令和という文字列が含まれていることのみを確認
        self.assertRegex(year, expected)
        
    def test_scrape_ques_num(self):
        _, ques_num, _ = ts.scrape_question_info(self.driver)
        expected = r"問\d+"
        self.assertRegex(ques_num, expected)
        
    def test_scrape_ques_num(self):
        _, _, opt_num = ts.scrape_question_info(self.driver)
        expected = r"肢\d+"
        self.assertRegex(opt_num, expected)
        
    def test_scrape_answer(self):
        answer = ts.scrape_correct_answer(self.driver)
        expected = r"(正|誤)"
        self.assertRegex(answer, expected)
        
    def test_scrape_explanation(self):
        kaisetsu = ts.scrape_explanation(self.driver)
        expected = r"(誤り|正しい|不適当|適当|違反する|違反しない)" # NOTE: 必要なテストケース全てを網羅できているわけではない
        self.assertRegex(kaisetsu, expected)

class TestSelectCategory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://takken-siken.com/marubatu.php')
                
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    # def test_select_main_category(self):
    #     checkbox = self.driver.find_element(By.XPATH, '//input[@name="fields[]" and @value="1"]')
    #     self.assertFalse(checkbox.is_selected())
    
    def test_toggle_check_all_on(self):
        # 全項目のチェックをONにする
        ts.toggle_check_all(self.driver, action="ON")
        
        # 全てのチェックボックスを取得し、すべてが選択されていることを確認
        all_checkboxes = self.driver.find_elements(By.XPATH, '//input[@name="fields[]"]')
        for checkbox in all_checkboxes:
            self.assertTrue(checkbox.is_selected(), f"カテゴリ {checkbox.get_attribute('value')} が選択されていません。")

    
    def test_toggle_check_all_off(self):
        ts.toggle_check_all(self.driver, action='OFF')

        all_checkboxes = self.driver.find_elements(By.XPATH, '//input[@name="fields[]"]')
        for checkbox in all_checkboxes:
            self.assertFalse(checkbox.is_selected(), f"カテゴリ {checkbox.get_attribute('value')} が選択されていますが、選択されていないべきです。")

    def test_select_main_categories(self):
        main_categories = ['1', '2']
        ts.select_main_categories(self.driver, main_categories)

        # 全てのメインカテゴリのチェックボックスを確認
        all_main_checkboxes = self.driver.find_elements(By.XPATH, '//input[@name="fields[]"]')

        # メインカテゴリが期待通りの状態か確認
        for checkbox in all_main_checkboxes:
            value = checkbox.get_attribute("value")
            if value in main_categories:
                self.assertTrue(checkbox.is_selected(), f"メインカテゴリ {value} が選択されていません")
            else:
                self.assertTrue(checkbox.is_selected(), f" メインカテゴリ {value} が選択されていますが、選択されているべきではありません")


# class TestClickButtons(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # クラス全体で一回だけwebdriverを初期化(setupメソッドは各テストメソッドの前に呼ばれる)
#         cls.driver = webdriver.Chrome()
#         cls.driver.get('https://takken-siken.com/marubatu.php')
        
#         ts.click_start_button(cls.driver)
        
#     @classmethod
#     def tearDownClass(cls):
#         # 全テスト後にwebdriverを終了
#         cls.driver.quit()

#     def test_click_pass_button(self):
#         self.assertEqual(1, 2) # パスボタンをクリックしたら、解説や正解が見えるようになるはずなので、そこでテストを書きたいはず。。。

# class TestButtonClick(unittest.TestCase):
#     def setUp(self):
#         self.driver = MagicMock()
        
#     def test_click_next_button(self):
#         ts.click_next_button(self.driver)
        
#         # find_elementが正しく呼ばれているかを確認
#         self.driver.find_element.assert_called_once_with(By.CSS_SELECTOR, 'button[data-text="NEXT"]')
        
#         # クリック操作が行われているかを確認
#         next_button_mock = self.driver.find_element.return_value
#         next_button_mock.click.assert_called_once()
        

# class TestCSVWriter(unittest.TestCase):
#     def setUp(self):
#         self.sample_data = [
#             {
#                 "year": "令和3年",
#                 "question_number": "問1",
#                 "option_number": "肢1",
#                 "question_text": "次の文は…",
#                 "option_text": "1. 選択肢1",
#                 "answer": "正",
#                 "kaisetsu": "この解説は…"
#             }
#         ]
        
#     @patch('builtins.open', new_callable=mock_open)
#     def test_csv_header(self, mock_file):
#         # ダミーのドライバを使ってテスト
#         driver = None
        
#         ts.write_data_to_csv(driver, num_questions=1, filename="dummy.csv")

#         # 書き込まれた内容を確認
#         mock_file.assert_called_once_with('dummy.csv', mode='w', newline='', encoding='utf-8')
#         handle = mock_file()
#         # ↓このテストがなぜか通らない。
#         handle.write.assert_any_call("year,question_number,option_number,question_text,option_text,answer,kaisetsu\n")


# class TestFlakyCode(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.get('https://takken-siken.com/marubatu.php')
#         ts.click_start_button(cls.driver)
        
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()  

#     def test_title(self):
#         for _ in range(20):
#             actual = self.driver.title
#             expected = '宅建士 一問一答道場🥋｜宅建試験ドットコム'
#             self.assertEqual(actual, expected)
#             ts.click_next_button(self.driver)



if __name__ == "__main__":
    unittest.main()