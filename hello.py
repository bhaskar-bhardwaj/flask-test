from flask import Flask
app = Flask(__name__)

@app.route('/admin')
def hello_world():
   return "Hello World"

@app.post('/fxn')
def test_fxn():
    return "Just test fxn"

if __name__ == '__main__':
   app.debug = True
   app.run()
