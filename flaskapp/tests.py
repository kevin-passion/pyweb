from flaskapp import app, Response, make_response, request, render_template, date, datetime, g, session , Markup
from flaskapp.classes import Nav

# @app.route("/")   # route에 URI를 정의한다. endpoint 
# def helloworld():
#     print("Hello flask.")
#     return "Hello World." 

@app.route("/gg")   # route에 URI를 정의한다. endpoint 
def helloworld2():
    print("Hello flask.")
    return "Hello World." + getattr(g, 'str', '111')  # 세번째 인자는 default value

# response_class
@app.route("/res")
def res():
    custom_res = Response("Custom Response", 201, {'test': 'ttt'})
    print("Response class.")
    return make_response(custom_res)

# str: Simple String(HTML, json)
@app.route("/res_simp")
def helloworld4():
    print("custom_response.")
    return make_response("custom response.")

@app.route("/test_wsgi")
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-type', 'text/plain'),
                   ('Content-Length', str(len(body)))]  
        start_response('200 OK', headers)
        return [body]
    return make_response(application)  # response 객체를 만들건데 application함수가 해줘


### Routing 

# @app.route('/test')
# @app.route('/test', methods=['POST','PUT'])
# @app.route('/test/<id>')
# @app.route('/test', defaults={'page':'index'})
# @app.route('/test/<page>')
# @app.route('/test', host='abc.com')  #도메인에 따른 분기 
# @app.route('/test', redirect_to='/new_test')   

@app.route('/rp')
def rp():
    q = request.args.get('q')
    return "q=%s" % str(q)

@app.route("/sd")
def sd():
    return "Hello local.com"

@app.route("/sd", subdomain='g')
def sd2():
    return "Hello G.Local.com..."

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans 


@app.route('/reqenv')
def reqenv():
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'   
        'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
        'PATH_INFO: %(PATH_INFO) s <br>'
        'QUERY_STRING: %(QUERY_STRING) s <br>'
        'SERVER_NAME: %(SERVER_NAME) s <br>'
        'SERVER_PORT: %(SERVER_PORT) s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
        # 'wsgi.version: %(wsgi.version) s <br>'
        # 'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
        # 'wsgi.input: %(wsgi.input) s <br>'
        # 'wsgi.errors: %(wsgi.errors) s <br>'
        # 'wsgi.mutithread: %(wsgi.mutithread) s <br>'
        # 'wsgi.mutiprocess: %(wsgi.mutiprocess) s <br>'
        # 'wsgi.run_once: %(wsgi.run_once) s'
        ) % request.environ

@app.route('/wc')
def wc():
    key = request.args.get('key')   
    val = request.args.get('val')
    res = Response('SET COOKIE')
    res.set_cookie(key, val)
    return make_response(res)    # http://local.com:5000/wc?key=jj&val=val99

@app.route('/rc')
def rc():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return "cookie['" + key + "] = " + val    # http://local.com:5000/rc?key=jj

@app.route('/wc2')
def wc2():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token']='123X'    # SECRET_KEY 와 함께 암호화되어 SESSION_COOKIE_NAME 으로 지정한 이름으로 암호화 결과값이 저장된다.
    return make_response(res)
    
@app.route('/rc2')    
def rc2():
    key=request.args.get('key')
    val=request.cookies.get(key)
    return "cookie['" + key +"'] = " + val + " , " + session.get("Token")   # 복호화된 값을 제공한다.


@app.route("/tmpl")
def t():
    tit = Markup("<h2>Title</h2>")
    print(">>>>>>>", type(tit))

    # component화 시키기 
    mu = Markup("<h1>iii=<i>%s</i></h1>")
    h = mu % "Italic"
    print("h = ", h)

    # Markup.escape() & unescape()
    bold = Markup("<b>Bold</b>")        # <b>Bold</b>
    bold_escape = Markup.escape("<b>Bold</bold>")  # &lt;b&gt;Bold&lt;/bold&gt;
    bold_unescape = bold_escape.unescape()   # <b>Bold</b>

    print(">>>", bold, bold_escape, bold_unescape)

    # For loop 
    # {% for var in iter %} ... {% endfor %}
    lst = {("지우개", "필기도구"), ("연필", "필기도구")}

    return render_template('index.html', \
        title=tit, bold = bold, bold_escape=bold_escape, \
        bold_unescape=bold_unescape, lst = lst    )

@app.route("/tmpl2")
def tmpl2():
    a = (1, '지우개', "필기도구", [])
    b = (2, '연필', '필기도구', [a])
    c = (3, '볼펜', '필기도구', [a,b])
    d = (4, '샤프심', '필기도구', [a,b,c])
    
    return render_template("index2.html", lst=[a,b,c,d])

@app.route("/tmpl3")
def tmpl3():
    py = Nav("파이썬","https://search.naver.com")
    java = Nav("자바", "https://search.naver.com")
    t_prg = Nav("프로그래밍 언어", "https://search.naver.com",[py, java])
    jinja = Nav("Jinja", "https://search.naver.com")
    t_flask = Nav("플라스크","https://search.naver.com",[jinja])

    return render_template("index2.html", navs=[t_prg, t_flask])

@app.route("/main")
def main():
    return render_template("main.html")


@app.route("/modal")
def modal():
    return render_template('modal.html')

