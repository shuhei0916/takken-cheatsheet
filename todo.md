## TODO:
- [ ] 不動産登記法に絞って解析を行う
    - [ ] カテゴリセレクタを作成する（後回し！）
        - [x] 全項目をOFFにする
        - [ ] メインカテゴリを選択する関数を定義する
        - [ ] サブカテゴリを選択する関数を定義する
    - [ ] スクレイピング処理の前にカテゴリを手動で選択するための待機時間を設ける。
- [x] logがgitignore出来ていない問題を解決する。
    - [x] ログの拡張子をlogにする。
- [ ] next_bottonをクリックするとき、稀に別の要素（広告など）をクリックしてしまう問題を解決する
    - [x] ページのタイトルをチェックし、間違っていれば戻るような実装を考える。
        - [ ] Confirm Form Resubmissionの問題を解決する。
    - [ ] nextボタンがクリックできるようになるまで待機するロジックを実装する
    - [ ] click_next_button()のロジックを見直す。
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


