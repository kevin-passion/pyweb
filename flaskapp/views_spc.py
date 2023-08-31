from collections import namedtuple
from flaskapp import app, request, render_template, datetime, relativedelta, timedelta, date
from flaskapp.models import User
from flaskapp.init_db import db_session, SQLAlchemyError, text

import os
from flask import Flask, g, request, Response, make_response
from flask import session, render_template, Markup, url_for, flash
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
# 모듈 path 추가
import sys
sys.path.append(r'C:\Python311\Lib\site-packages')


# SPC TEST : class, def 를 import해야 한다.
# from lrt import LRT_chart, LRT, LRT_chart_bokeh
from spc_rules import nelson_rules_exam, nelson_rules_check, spcRuleAnomalyDetector

# chart 출력
import io
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
import base64
from flask import redirect

# bokeh chart 출력
import random
# from bokeh.embed import components
# from bokeh.plotting import figure



#DB접속
# import mariadb
import sys

# file upload
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

# from .database import db_conn


#-----------------------------------------------
# 2-3) SPC 관리도 (X - mR, X바 - R, X바 - S ) TEST
#-----------------------------------------------
# SCP Rule Check : 메뉴로딩시 적용
@app.route('/spc/spc_check')
def spc_check():

    l_chart, l_data = nelson_rules_exam("spc_rule1")
    print(f' ldata : {l_data}', {len(l_data)})

    return render_template("/spc/spc_check.html", l_chart = l_chart, l_data = l_data, rule_no = 'spc_rule1', outlier_yn='N')


# SCP Rule Check : : 읽은 파일의 선택한 컬럼명으로 LRT작성 
@app.route('/spc/rule_col', methods=['POST'])    
def rule_col():
    filename    = request.form['filename']
    subgroup     = request.form['subgroup']
    colname     = request.form['colname']
    rule_no     = request.form['rule_no']

    data = request.form['data']
    print(f'>>>> data : {data}')


    # 공백 문자열이 있으면  변경 
    subgroup = subgroup.replace(' ','|')
    colname = colname.replace(' ','|')

    #menu        = request.form['menu']
    print(f' >>>> /spc/rule_col -- filename : {filename}, subgroup : {subgroup}, colname : {colname}, rule_no : {rule_no}')
    return redirect(url_for('spc_rule_draw', name=filename, subgroup=subgroup, colname=colname, rule_no=rule_no)) 


# SPC Rule Check 검사 진행 : 메뉴 > SCP Rule Check
@app.route('/spc/rule_check', methods=['POST'])
def rule_check():
    filename    = request.form['filename']
    subgroup     = request.form['subgroup']
    colname     = request.form['colname']
    rule_no     = request.form['rule_no']

    # 공백 문자열이 있으면  변경 
    subgroup = subgroup.replace(' ','|')
    colname = colname.replace(' ','|')

    #menu        = request.form['menu']
    print(f' >>>> /spc/rule_check -- filename : {filename}, subgroup : {subgroup}, colname : {colname}, rule_no : {rule_no}')
    return redirect(url_for('spc_rule_draw', name=filename, subgroup=subgroup, colname=colname, rule_no=rule_no)) 

# SPC RULE CHECK 작성하기 : 이미지 생성 및 전달           
# @app.route('/rule_uploads/<name> <subgroup> <colname> <rule_no>')    
# def spc_rule_draw(name=None, subgroup=None, colname=None, rule_no=None):

#     print(f' >>>> spc_rule_draw -- filename : {name}, subgroup:{subgroup},colname:{colname},rule_no:{rule_no}')

#     # 변경된 문자열이 있으면 원래대로 변경 
#     subgroup = subgroup.replace('|',' ')
#     colname = colname.replace('|',' ')

#     # 업로드된 파일 URL로 전달하기 
#     try:

#         if name.rsplit(".", 1)[1].lower() == 'xlsx':
#             data = pd.read_excel(f"{os.path.join(app.config['UPLOAD_FOLDER'], name)}")  # 파일읽기 
#         else:
#             data = pd.read_csv(f"{os.path.join(app.config['UPLOAD_FOLDER'], name)}")  # 파일읽기 
            
#         df_to_html = data.to_html(border=1, justify='center', col_space=80 )        # html로 변환하여 보여줌

#         # 첨부파일의 컬럼명 list하여 URL로 전달하기 
#         #col_names = list(data.columns)
#         # 전체 데이터 컬럼  
#         col_names_all = list(data.columns)

#         # 부분군(subgroup) 대상 컬럼만 출력하기
#         sub_groups = getSubGroupColumns(data)
#         print(f' >>>>> sub_groups : {sub_groups}')

#         # 숫자형 컬럼명만 추출
#         col_names = getFloatColumns(data)
#         print(f' <<< col_names : {col_names}')

#         # subgroup대상인 경우에는 col_names에서 제외하기 
#         # 단, 컬럼이 1개 일 때 에는 제외 
#         if len(sub_groups) != 0 or len(col_names) != 0:
#             for s in sub_groups:
#                 # col_names.remove(s)
#                 col_names = [col for col in col_names if col not in sub_groups]
        
#         print(f' <<< 최종 col_names : {col_names}')
        
#         # 수신된 colname으로 데이터를 분리하여 chart작성 준비 
#         #print(f' RRRR  --> colname : {colname} , subgroup : {subgroup}')
#         #result = filter(lambda x : x != 0, data[colname] )                          # 해당 레코드로 읽기
#         #spc_data = pd.Series(list(result))

#         # 받은 파일을 이용한 SPC RULE 테스트 
#         print(f' <<< 받은 파일을 이용한 SPC RULE 테스트 start ....... ')
#         #nelson_rules_check(rule_no, data, subgroup, colname)
#         spc_chart, outlier_y = nelson_rules_check(rule_no, data, subgroup, colname)
#         #nelson_rules_check(rule_no, data, subgroup, colname)
#         #nelson_rules_check(rule_no, data, "week", "amount")
#         print(f" >>>>> outlier_y : {outlier_y}")

#         # 이미지 생성
#         l_chart, l_data = nelson_rules_exam(rule_no)
#         print(f" >>>>> l_data : {l_data}")
        
#         if len(outlier_y) > 3 or len(l_data) > 5:
#             outlier_yn = 'Y'
#             print(f'outlier data가 있습니다.')
#         else:
#             outlier_yn = 'N'
#             print(f' >>>>>> NO outlier data....')

#         # URL로 응답하기
#         # l_chart : default LRT chart, l_data : default LRT Ratio
#         # filename : 업로드 파일명, read_file : 업로드 파일내용
#         # l_chart2 : 업로드 파일의 LRT chart, l_data2 : 업로드 파일의 LRT Ratio
#         # col_names : 업로드 파일 컬럼명 List, colname : 업로드 파일 선택된 컬럼명
#         # rule_no : spc check rule no
#         return render_template('/spc/spc_check.html', l_chart = l_chart, l_data = l_data, 
#                                 filename=name, read_file=df_to_html,
#                                 sub_groups=sub_groups, subgroup=subgroup,
#                                 col_names=col_names, colname=colname,
#                                 spc_chart=spc_chart, outlier_y=outlier_y, outlier_yn=outlier_yn,
#                                 rule_no=rule_no, data=pd.DataFrame(data))
    
#     except Exception as e:
#         print(f' >>>>>>>>>>> except 발생')
#         print(f'caught {type(e)}: e')
#         print(f' >>>> spc_rule_draw -- filename : {name}')
#         print(f' >>>>>>>>>>> rule_no : {rule_no}')
#         l_chart, l_data = nelson_rules_exam(rule_no)
#         return render_template("/spc/spc_check.html", l_chart = l_chart, filename=name, l_data = l_data, rule_no = rule_no, outlier_yn='N')
    

# SCP Excel Table : Data Table
# @app.route('/spc/data_table', methods=['GET', 'POST'])
# def data_table():

#     # First Chart - Scatter Plot
#     p1 = figure(height=350, sizing_mode="stretch_width")
#     p1.circle(
#         [i for i in range(10)],
#         [random.randint(1, 50) for j in range(10)],
#         size=20,
#         color="navy",
#         alpha=0.5
#     )
  
#     # Second Chart - Line Plot
#     language = ['Python', 'JavaScript', 'C++', 'C#', 'Java', 'Golang']
#     popularity = [85, 91, 63, 58, 80, 77]
  
#     p2 = figure(
#         x_range=language,
#         height=350,
#         title="Popularity",
#     )
#     p2.vbar(x=language, top=popularity, width=0.5)
#     p2.xgrid.grid_line_color = None
#     p2.y_range.start = 0
  
#     # Third Chart - Line Plot
#     p3 = figure(height=350, sizing_mode="stretch_width")
#     p3.line(
#         [i for i in range(10)],
#         [random.randint(1, 50) for j in range(10)],
#         line_width=2,
#         color="olive",
#         alpha=0.5
#     )

#     p4 = LRT_chart_bokeh()

  
#     script1, div1 = components(p1)
#     script2, div2 = components(p2)
#     script3, div3 = components(p3)
#     script4, div4 = components(p4)
    
#     # 
#     if request.method == 'POST':
#         print(request.files['file'])
#         f = request.files['file']
#         if f.filename.rsplit(".", 1)[1].lower() == 'xlsx':
#             data_xls = pd.read_excel(f)
#         else:
#             data_xls = pd.read_csv(f)
#         #print(f'excel data :{data_xls}')
#         #return data_xls.to_html()

#         return render_template("/spc/data_table.html", data_xls=data_xls,
#                             script=[script1, script2, script4],
#                             div=[div1, div2, div3, div4],)
#     # return '''
#     # <!doctype html>
#     # <title>Upload an excel file</title>
#     # <h1>Excel file upload</h1>
#     # <form action="" method=post enctype=multipart/form-data>
#     # <p><input type=file name=file><input type=submit value=Upload>
#     # </form>
#     # '''
#     #return render_template("/spc/data_table.html", l_chart = l_chart, l_data = l_data, rule_no = 'spc_rule1', outlier_yn='N')
#     return render_template("/spc/data_table.html", data_xls=pd.DataFrame({'name':['NoData']}),
#                         script=[script1, script2, script3, script4],
#                         div=[div1, div2, div3, div4],)


# @app.route('/spc/bokeh')
# def bokeh():
#     # First Chart - Scatter Plot
#     p1 = figure(height=350, sizing_mode="stretch_width")
#     p1.circle(
#         [i for i in range(10)],
#         [random.randint(1, 50) for j in range(10)],
#         size=20,
#         color="navy",
#         alpha=0.5
#     )
  
#     # Second Chart - Line Plot
#     language = ['Python', 'JavaScript', 'C++', 'C#', 'Java', 'Golang']
#     popularity = [85, 91, 63, 58, 80, 77]
  
#     p2 = figure(
#         x_range=language,
#         height=350,
#         title="Popularity",
#     )
#     p2.vbar(x=language, top=popularity, width=0.5)
#     p2.xgrid.grid_line_color = None
#     p2.y_range.start = 0
  
#     # Third Chart - Line Plot
#     p3 = figure(height=350, sizing_mode="stretch_width")
#     p3.line(
#         [i for i in range(10)],
#         [random.randint(1, 50) for j in range(10)],
#         line_width=2,
#         color="olive",
#         alpha=0.5
#     )
  
#     script1, div1 = components(p1)
#     script2, div2 = components(p2)
#     script3, div3 = components(p3)
  
#     # Return all the charts to the HTML template
#     return render_template(
#         template_name_or_list='/spc/data_table.html',
#         script=[script1, script2, script3],
#         div=[div1, div2, div3],
#     )

