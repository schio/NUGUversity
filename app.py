from flask import Flask
from flask import request
from pprint import pprint as p
import json
import dbWorks
import getLibraryInfo

app = Flask(__name__)

@app.route('/nugu/<svc>', methods=['POST'])
def start(svc):
    data = request.json
    isError = False

    # actionData
    action = data['action']
    params = action['parameters']
    actionName = action['actionName']

    # 학식 가격
    if actionName == 'answer.meal_price':
        mm = params['meal_name']
        name = mm['value']
        return_v = meal_price(name)
        result = {return_v[0]: return_v[1]}

    # 학식 메뉴(식당별)
    elif actionName == 'answer.which_cafeteria':
        which = params['which_2']
        name = which['value']
        return_v = which_cafeteria(name)
        if return_v:
            result = {return_v[0]: return_v[1]}
        else:
            isError = True

    # 학식 메뉴(식당별, 날짜별))
    elif actionName == 'answer.which_when_cafeteria':
        which = params['which']
        when = params['when']
        name = which['value']
        day = when['value']
        return_v = which_when_cafeteria(name, day)
        if return_v:
            result = {return_v[0]: return_v[1]}
        else:
            isError = True

    # n 열람실 좌석 정보 가져오기
    elif actionName == 'answer.which_library_seat':
        library_class = params['library_class']
        library_class = library_class['value']
        return_v = which_library_seat(library_class)
        if return_v:
            result = {return_v[0]: return_v[1]}
        else:
            isError = True


    # 케이스가 없는 경우
    else:
        isError = True

    # 결과 반환
    if isError == False:
        result_dict = {
            "version": "2.0",
            "resultCode": "OK",
            "output": result,
        }
    else:
        result_dict = {
            "version": "2.0",
            "resultCode": "Error"
        }
    return json.dumps(result_dict)


def meal_price(name):
    return ('price', '4500')

def which_cafeteria(name):
    if name == '군자관':
        text = dbWorks.getGunja('TODAY')
        return ('menu_2', text)

def which_when_cafeteria(name, day):
    if name == '군자관':
        text = dbWorks.getGunja(day)
        return ('menu', text)

def which_library_seat(library_class):
    text = getLibraryInfo.getEmptySeats(library_class)
    return text

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'
 
 
if __name__ == '__main__':
    app.run()