from flask import Flask, render_template, session, request, redirect, url_for
import os

# インスタンスの生成
app = Flask(__name__)

# セッションで使う鍵を設定
key = os.urandom(21)
app.secret_key = key

import eng_prac_app.views