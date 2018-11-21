from flask import Flask
from flask import request
from pprint import pprint as p

app = Flask(__name__)
 
@app.route('/nugu/<svc>', methods=['POST'])
def start(svc):
    data = request.json

    # actionData
    action = data['action']

    if action['actionName'] == 'answer.meal_price':
        params = action['parameters']
        p(params)
        mm = params['meal_name']
        p(mm)
        data = mm['value']
        p(data)
        result = meal_price(data)

    elif action['actionName'] == 'answer.which_cafeteria':
        result = 0

    return result

def meal_price(name):
    return 4500

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'
 
 
if __name__ == '__main__':
    app.run()