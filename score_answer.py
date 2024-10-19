def score_answer(text, correct_keywords, incorrect_keywords):
    # 形態素解析で単語を取得
    tokens = tokenize_text(text)
    
    # スコアの初期化
    score = 0
    
    # 正解に多く含まれる単語でスコアを加算
    for token in tokens:
        if token in correct_keywords:
            score += 1
        elif token in incorrect_keywords:
            score -= 1
    
    return score

# 正解と誤りの単語リスト（相対的に頻出するもの）
correct_keywords = ['登記', '申請', '所有', '権利', '建物', '定め', '承継', '法人', '滅失']
incorrect_keywords = ['提供', '識別', '代位', '区域', '納付', '複数', '規定', '買い受け']

# テスト用の選択肢
test_text = "登記申請は所有権の移転に関するものである。"

# スコアを計算
score = score_answer(test_text, correct_keywords, incorrect_keywords)

# スコアが正の数なら正解の可能性、負の数なら誤りの可能性が高い
if score > 0:
    print("この選択肢は正解の可能性が高いです。")
elif score < 0:
    print("この選択肢は誤りの可能性が高いです。")
else:
    print("正解・誤りの判断が難しいです。")
