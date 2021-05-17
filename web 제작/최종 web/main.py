# -*- coding: utf-8 -*-
# 기본 템플릿
from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
from flask import Flask
from flask import redirect


# 서버역할을 할 객체 생성
app = Flask(__name__)

# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/')
def home():    
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)