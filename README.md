# 英単語練習アプリ by Flask
Flaskの練習用に作成した英単語練習サイトです。  


## サイト概要
登録されたランダムに3問選択し、日本語と英単語の品詞を出題します。  
対応する英単語を入力すると、正解と正解数を表示します。 
現在登録している英単語は `/data/english_words.csv` にベタ書きしている10単語のみです... 


## サイト詳細
サイトを開くとログインを求められます。  
現在は `/data/id_pass.txt` にベタ書きしたid, passを用いて認証しています...(今後アップデート予定)  
![ログイン](https://github.com/DogsCox/english_word_practice_flask_webapp/blob/images/login.png "login")  

ログインするとメニュー画面になります。  
"英単語の練習をする" をクリックすると英単語練習画面に行きます。  
![index](https://github.com/DogsCox/english_word_practice_flask_webapp/blob/images/index.png "index")  

英単語練習画面です。  
3問出題されるので、それぞれ回答します。  
![problems](https://github.com/DogsCox/english_word_practice_flask_webapp/blob/images/problems.png "problems")  

回答すると正解と正解数が表示されます。  
![answers](https://github.com/DogsCox/english_word_practice_flask_webapp/blob/images/answer.png "answers")


## アップデート情報
2021/7/24: v0.1リリース。最低限の機能のみ実装。  

今後対応予定  

- ログイン認証機能
- DB連携。英単語をDBに格納。
- DBへ新規に単語登録する機能
- html, cssのブラッシュアップ。見た目をまともにする。
