from flask import Flask
 
app = Flask(__name__)
 
 
<<<<<<< HEAD
@app.route('/start')
def start():
    return 'start'
 
 
@app.route('/select/<name>')
def select(name):
    return 'hi %s' % name
 
=======
@app.route('/nugu/<svc>')
def start(svc):
    return 'type : %s' % svc
>>>>>>> c645cbbdb42d90b14e90e938673761bf26fc545b
 
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'
 
 
if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run()
>>>>>>> c645cbbdb42d90b14e90e938673761bf26fc545b
