# TODO:
## TDD:
- [ ] next_bottonをクリックするとき、稀に別の要素（広告など）をクリックしてしまう問題を解決する
    - [ ] nextボタンがクリックできるようになるまで待機するロジックを実装する
    - [ ] click_next_button()のロジックを見直す。
    - [ ] ページのタイトルをチェックし、間違っていれば戻るような実装を考える。
    - [ ] adblockerを入れる
- [ ] csvファイルにまとめる部分を書く
    - [x] mockについて調べる（assert_called_once_withとか）
    - [x] csvファイルにヘッダーを書き込む
    - [ ] スクレイピングによって取得したデータをcsvファイルに書き込む


## Other:
- [ ] 異常系のテストも書く
- [ ] エラーハンドリングを書く
- [ ] webdriver.wait, staleelementReferenceExceptionについてもう少し調べる(https://www.seleniumqref.com/api/python/conditions/Python_element_to_be_clickable.html
)


## 全体の流れ:
前半：スクレイピングによる宅建の過去問の取得
後半：過去問の解析（形態素解析など）


