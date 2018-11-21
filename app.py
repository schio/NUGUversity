from flask import Flask
from flask import request
from pprint import pprint as p

app = Flask(__name__)
def get_leaf_dict( dict, key_list):
    res=dict
    for key in key_list:
        res=dict.setdefault( key, {} )
    return res

@app.route('/nugu/<svc>', methods=['POST'])
def start(svc):
    data = request.json

    # actionData
    action = data['action']
    params = action['parameters']
    actionName = action['actionName']

    # 학식 가격
    if actionName == 'answer.meal_price':
        mm = params['meal_name']
        name = mm['value']
        result = meal_price(name)

    # 학식 메뉴(식당별)
    elif actionName == 'answer.which_cafeteria':
        which = params['which_2']
        name = which['value']
        result = which_cafeteria(name)

    # 학식 메뉴(식당별, 날짜별))
    elif actionName == 'answer.which_when_cafeteria':
        which = params['which']
        when = params['when']
        name = which['value']
        day = when['value']
        result = which_when cafeteria(name, day)

    result_dict = {
        "version": "2.0",
        "resultCode": "OK",
        "output": result,
    }
    return result_dict


def meal_price(name):
    return {'price': '4500'}

def which_cafeteria(name):
    return {'menu_2': '동까스'}

def which_when_cafeteria(name, day):
    return {'menu': '동까스2'}

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'
 
 
if __name__ == '__main__':
    app.run()