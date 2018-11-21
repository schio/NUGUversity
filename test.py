from flask import Flask

app = Flask(__name__)

@app.route('/nugu/<svc>')
def start():
    return 'start %s' % svc

if __name__ == '__main__':
    app.run(debug=True)