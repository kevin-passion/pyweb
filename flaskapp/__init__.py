# webapplication을 구동하는 파일 
# 여기에서 import 하는 class 함수는 가동과 함께 시작된다.
# g: 전역변수
# WSGI: web server gateway interface

from datetime import date, datetime, timedelta
from flask import Flask, g, Response, \
        make_response, render_template, \
        request, session, Markup, url_for, flash
from dateutil.relativedelta import relativedelta
import os
# from flaskapp.init_db import init_database, db_session, text

app = Flask(__name__)  # Flask 생성 
import flaskapp.views
import flaskapp.tests
import flaskapp.filters
import flaskapp.classes
import flaskapp.utils
import flaskapp.models


import pandas as pd
import numpy as np
import sys 

app.debug = True

# server_name를 도메인 사용으로 지정하면 ip로는 연결되지 않는다. 
# app.config['SERVER_NAME'] = 'local.com:5001'   # hosts에 localhost로 등록한 이름 
app.config['SERVER_NAME'] = '127.0.1.1'   # hosts에 localhost로 등록한 이름 


# jinja 사용구문에서 개행되는 것을 방지  
app.jinja_env.trim_blocks = True 


### Session     
app.config.update(
    SECRET_KEY = 'X1243yRH!mNwf',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31)
)

# @app.before_first_request # 첫번째 요청을 부를 때 실행.
# @app.before_request       # 매번 요청을 부를 때 마다 실행 (router가 model에게 전달하기 전, 대표적 web filter )
# @app.after_request        # 요청을 실행 후에 실행 
# @app.teardown_request     # stream으로 내린 후 destroy 될때 실행 
# @app.teardown_appcontext  # application context destroy 될때 실행 

## linux apche 환경의 flask 테스트 환경에서 DB 제외 
# @app.before_request
# def beforeFist():
#     print(">> before_first_request!!!")
#     g.str = "한글"
#     init_database()

# @app.after_request
# def afterReq(response):
#     print(">> after_request!!")
#     return response

# # Request가 끝났을 때 실행 
# @app.teardown_request
# def teardown_request(exception):
#     print(">>> teardown request!!", exception)

# # response까지 끝났을 때 처리 
# @app.teardown_appcontext
# def teardown_context(exception):
#     print(">>> teardown context!!", exception)
#     db_session.remove()

@app.route("/")
def idx():
    # rds = []
    # for i in [1,2,3]:
    #     id = 'r' + str(i)
    #     name = 'radiotest'
    #     value = i
    #     checked = ''
    #     if i ==2:
    #         checked = 'checked'
    #     text = 'RadioTest' + str(i)
    #     rds.append( FormInput(id, name, value, checked, text))
    return render_template("app.html", ttt='Test param')



