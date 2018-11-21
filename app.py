from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/nugu/<svc>')
def start(svc):
    return 'type : %s' % svc
 
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'
 
 
if __name__ == '__main__':
    app.run()