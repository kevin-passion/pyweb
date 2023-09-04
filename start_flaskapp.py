from flaskapp import app

app.run(host= '0.0.0.0', port=5000, debug=True)   # apache가 기동하면서 이곳의 app.run은 대체 된다. 
# app.run(port=5000, debug=True)