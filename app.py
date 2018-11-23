from flask import Flask
from flask import request
from pprint import pprint as p
import json
import dbWorks
import getLibraryInfo
import shortUrlN

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
            ratio = float(return_v[1]) / float(return_v[0])
            if ratio > 0.6:
                ratio_status = 'low'
            elif ratio > 0.3:
                ratio_status = 'middle'
            else:
                ratio_status = 'high'
            result = {'total_seats': return_v[0], 'empty_seats': return_v[1], 'status': ratio_status}
        else:
            isError = True

    # 전화번호 알아내기
    elif actionName == 'answer.phone_book':
        dept_name = params['dept_name']
        dept_name = dept_name['value']
        return_v = phone_book(dept_name)
        if return_v:
            result = {return_v[0]: return_v[1]}
        else:
            isError = True
        
    # 운영시간 알아내기
    elif actionName == 'answer.dept_time':
        dept_name = params['name_dept_time']
        dept_name = dept_name['value']
        return_v = dept_time(dept_name)
        if return_v:
            result = {return_v[0]: return_v[1], return_v[2]: return_v[3]}
        else:
            isError = True

    # 공지사항 가져오기
    elif actionName == 'answer.get_notice':
        return_v = dbWorks.getNotice()
        result = {
            'first': return_v[0],
            'second': return_v[1],
            'third': return_v[2],
            'second': return_v[3],
            'second': return_v[4]
        }

    elif actionName == 'answer.get_detail_notice':
        notice_index = params['index']
        notice_index = notice_index['value']
        data = get_detail_notice(notice_index)
        return data


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

def get_detail_notice(index):
    # 데이터 가져오기

    # 문자 보내기

    # text 생성

def meal_price(name):
    mealPrice = dbWorks.getStudentsBuildingPrice(name)
    return ('price', mealPrice)

def which_cafeteria(name):
    if name == '군자관':
        text = dbWorks.getGunja('TODAY')
        return ('menu_2', text)

def which_when_cafeteria(name, day):
    if name == '군자관':
        text = dbWorks.getGunja(day)
        return ('menu', text)

def which_library_seat(library_class):
    return getLibraryInfo.getEmptySeats(library_class)
    
def phone_book(dept_name):
    phone_number = dbWorks.getTelBook(dept_name)
    phone_number = numToKorean(phone_number)
    return ('phone_number', phone_number)

def dept_time(dept_name):
    data = dbWorks.getDeptTime(dept_name)
    if len(data) == 2:
        return ('open_time', data[0], 'close_time', data[1])
    else:
        return ('open_time', data, 'close_time', '')

# 숫자 => 한글 (전화번호 tts)
def numToKorean(n):
    koreans = ['공', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    text = ""
    for i in str(n):
        text += koreans[int(i)]
    return text

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><input type="textbox"/>'

@app.route('/url')
def url():
    return shortUrlN.create()


if __name__ == '__main__':
    app.run()