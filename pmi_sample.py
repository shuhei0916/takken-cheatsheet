import MeCab
from collections import defaultdict, Counter
import pandas as pd
import numpy as np

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

# テキストから共起行列を作成する関数
def create_cooccurrence_matrix(texts, window_size=2):
    cooccurrence = defaultdict(Counter)
    for tokens in texts:
        for i in range(len(tokens)):
            for j in range(max(0, i - window_size), min(len(tokens), i + window_size + 1)):
                if i != j:
                    cooccurrence[tokens[i]][tokens[j]] += 1
    return cooccurrence

# PMIを計算する関数
def calculate_pmi(cooccurrence_matrix, total_count):
    pmi_matrix = defaultdict(dict)
    word_counts = Counter()
    for word, context in cooccurrence_matrix.items():
        word_counts[word] += sum(context.values())
    
    for word, context in cooccurrence_matrix.items():
        for co_word, co_occurrence in context.items():
            prob_word = word_counts[word] / total_count
            prob_co_word = word_counts[co_word] / total_count
            prob_co_occurrence = co_occurrence / total_count
            pmi_matrix[word][co_word] = np.log(prob_co_occurrence / (prob_word * prob_co_word))
    
    return pmi_matrix

# 正解と誤りの選択肢に分離
correct_answers = data[data['answer'] == '正']
incorrect_answers = data[data['answer'] == '誤']

# 正解と誤りの選択肢を形態素解析し、トークン化
correct_tokens = [tokenize_text(text) for text in correct_answers['option_text']]
incorrect_tokens = [tokenize_text(text) for text in incorrect_answers['option_text']]

# 正解の選択肢の共起行列を作成
correct_cooccurrence_matrix = create_cooccurrence_matrix(correct_tokens)

# 共起行列全体での単語の総出現回数を計算
total_word_count = sum(sum(context.values()) for context in correct_cooccurrence_matrix.values())

# PMIを計算
pmi_matrix = calculate_pmi(correct_cooccurrence_matrix, total_word_count)

# 結果の表示
for word, context in pmi_matrix.items():
    print(f"Word: {word}")
    for co_word, pmi in sorted(context.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  Co-occurs with {co_word}: PMI={pmi:.2f}")
    print()
