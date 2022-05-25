from flask import Flask, render_template, session, request, redirect, url_for
from pathlib import Path
import os
from eng_prac_app import app
from eng_prac_app.scripts.eng_question import send_eng_ja_pair


# ランディングページ
@app.route("/")
def index():
    if not session.get("login"):
        return redirect(url_for("login"))
    else:
        return render_template("index.html")


# ログインページ
@app.route("/login")
def login():
    return render_template("login.html")


# ログイン認証
@app.route("/logincheck", methods=["POST"])
def logincheck():
    user_id = request.form["user_id"]
    password = request.form["password"]

    # /data/id_pass.txtからIDとパスワードを読み込む
    valid_users = {}
    with open("./data/id_pass.txt", 'r', encoding="utf-8") as f:
        for row in f:
            id, pw = row.rstrip().split(",")
            valid_users[id] = pw

    # 認証
    if user_id in valid_users.keys():
        if password == valid_users[id]:
            session["login"] = True
        else:
            session["login"] = False
    else:
        session["login"] = False

    # 認証の状態に応じてリダイレクト
    if session["login"]:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))


# ログアウト
@app.route("/logout")
def logout():
    session.pop("login", None)
    return redirect(url_for("index"))


# 英単語練習回答ページ
@app.route("/eng_prac")
def eng_prac():
    # 英単語辞書ファイルへのpath
    path = Path()
    path = path.cwd() / "data" / "english_words.csv"
    path = path.resolve()
    probs = send_eng_ja_pair(path)
    session["probs"] = probs
    return render_template("eng_prac.html", problems=probs)


# 英単語練習正解チェックページ
@app.route("/anscheck", methods=["POST"])
def anscheck():
    user_ans = request.form.getlist("words")
    probs = session.get("probs")
    # 出題順序と同じになるようにsort
    probs = sorted(probs, key=lambda x: x['ord'])

    # ユーザの回答結果
    result = []
    # ユーザの正解数
    correct_num = 0
    for i, w in enumerate(user_ans):
        if w == probs[i]["word"]:
            result += "正解"
            correct_num += 1
        else:
            result += "不正解"
    return render_template(
        "result.html",
        correct=correct_num,
        ans=zip(probs, user_ans)
    )
