import MeCab
from collections import Counter
import pandas as pd
from pprint import pprint

# CSVファイルの読み込み
data = pd.read_csv('data/sample.csv')

# MeCabの辞書パスとmecabrcファイルのパスを指定
mecab = MeCab.Tagger('-r /home/shuhei0916/projects/takken-cheatsheet/.venv/lib/python3.10/site-packages/ipadic/dicdir/mecabrc -d /home/shuhei0916/projects/takken-cheatsheet/.venv/lib/python3.10/site-packages/ipadic/dicdir')

# 形態素解析を行う関数
def tokenize_text(text):
    node = mecab.parseToNode(text)
    words = []
    while node:
        if node.feature.startswith("名詞") or node.feature.startswith("動詞") or node.feature.startswith("形容詞"):
            words.append(node.surface)
        node = node.next
    return words

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

# 両方に含まれる単語の差分を計算
word_diff = {}
for word in correct_word_count:
    if word in incorrect_word_count:
        word_diff[word] = correct_word_count[word] - incorrect_word_count[word]

# 正解に多く含まれ誤りには少ない単語、またはその逆を抽出
correct_only_words = {word: correct_word_count[word] for word in correct_word_count if word not in incorrect_word_count}
incorrect_only_words = {word: incorrect_word_count[word] for word in incorrect_word_count if word not in correct_word_count}

# 出力
print("\nWords that appear more frequently in correct answers (relative difference):")
pprint(sorted(word_diff.items(), key=lambda x: x[1], reverse=True)[:10])

print("\nWords that appear more frequently in incorrect answers (relative difference):")
pprint(sorted(word_diff.items(), key=lambda x: x[1])[:10])

print("\nWords only found in correct answers:")
pprint(correct_only_words)

print("\nWords only found in incorrect answers:")
pprint(incorrect_only_words)


# 結果をデータフレーム化してCSVに出力（必要に応じて）
correct_df = pd.DataFrame(correct_word_count.most_common(), columns=['Word', 'Frequency'])
incorrect_df = pd.DataFrame(incorrect_word_count.most_common(), columns=['Word', 'Frequency'])

# CSVに保存
correct_df.to_csv('data/correct_word_frequencies.csv', index=False, encoding='utf-8-sig')
incorrect_df.to_csv('data/incorrect_word_frequencies.csv', index=False, encoding='utf-8-sig')
