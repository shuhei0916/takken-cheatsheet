import unittest
from unittest.mock import mock_open, patch
import csv

class TestFileWriting(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        # ファイルに書き込む処理
        with open('dummy.csv', 'w') as f:
            f.write('hello,world\n')
        
        # ファイルが開かれたかどうかを確認
        mock_file.assert_called_once_with('dummy.csv', 'w')
        
        # 書き込まれた内容を確認
        mock_file().write.assert_called_once_with('hello,world\n')

if __name__ == '__main__':
    unittest.main()
