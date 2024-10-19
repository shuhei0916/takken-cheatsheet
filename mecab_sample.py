import MeCab
from collections import Counter
import pandas as pd

# CSVファイルの読み込み
data = pd.read_csv('path_to_your_file.csv')

# MeCabの辞書パスとmecabrcファイルのパスを指定
mecab = MeCab.Tagger('-r /home/shuhei0916/projects/takken-cheatsheet/.venv/lib/python3.10/site-packages/ipadic/dicdir/mecabrc -d /home/shuhei0916/projects/takken-cheatsheet/.venv/lib/python3.10/site-packages/ipadic/dicdir')

# 形態素解析を行う関数
def tokenize_text(text):
    return mecab.parse(text).split()

# 正解と誤りの選択肢に分離
correct_answers = data[data['answer'] == '正']
incorrect_answers = data[data['answer'] == '誤']

# 正解と誤りの選択肢を形態素解析し、トークン化
correct_tokens = [tokenize_text(text) for text in correct_answers['option_text']]
incorrect_tokens = [tokenize_text(text) for text in incorrect_answers['option_text']]

# リストをフラット化
correct_tokens_flat = [token for sublist in correct_tokens for token in sublist]
incorrect_tokens_flat = [token for sublist in incorrect_tokens for token in sublist]

# 単語の頻度をカウント
correct_word_count = Counter(correct_tokens_flat)
incorrect_word_count = Counter(incorrect_tokens_flat)

# 正解と誤りでそれぞれ頻出する単語を表示
print("Most common words in correct answers:", correct_word_count.most_common(10))
print("Most common words in incorrect answers:", incorrect_word_count.most_common(10))

# 結果をデータフレーム化してCSVに出力（必要に応じて）
correct_df = pd.DataFrame(correct_word_count.most_common(), columns=['Word', 'Frequency'])
incorrect_df = pd.DataFrame(incorrect_word_count.most_common(), columns=['Word', 'Frequency'])

# CSVに保存
correct_df.to_csv('correct_word_frequencies.csv', index=False)
incorrect_df.to_csv('incorrect_word_frequencies.csv', index=False)
