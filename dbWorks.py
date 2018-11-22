# -*- coding: utf-8 -*-
import pymysql
import getMeal
from pprint import pprint as p
from datetime import datetime
from datetime import timedelta
def getDB():
    db = pymysql.connect(
            host='schio.iptime.org',
            port=3306,
            user='root',
            passwd='cldh1004',
            db='NUGUversity',
            charset='utf8'
        )
    return db

def getDay(day):

    if day=='TODAY':
        today=datetime.today()
        year=str(today.year)
        date=str(today.month)+'월'+ str(today.day)+'일'
    elif day=='TOMORROW':
        tomorrow=datetime.today() + timedelta(days=1)
        year=str(tomorrow.year)
        date=str(tomorrow.month)+'월' + str(tomorrow.day)+'일'
    elif day=='A_TOMORROW':
        twoDaysLater=datetime.today() + timedelta(days=2)
        year=str(twoDaysLater.year)
        date=str(twoDaysLater.month)+'월'+ str(twoDaysLater.day)+'일'
    elif day=='YESTERDAY':
        yesterday=datetime.today() - timedelta(days=1)
        year=str(yesterday.year)
        date=str(yesterday.month)+'월'+ str(yesterday.day)+'일'
    elif day=='B_YESTERDAY':
        dayBeforeYesterday=datetime.today() - timedelta(days=2)
        year=str(dayBeforeYesterday.year)
        date=str(dayBeforeYesterday.month)+'월'+ str(dayBeforeYesterday.day)+'일'
    return year,date

def saveGunja():
    db=getDB()
    cursor = db.cursor()
    gunjaDatas=getMeal.getGunja()
    # mealGunja Columns -> idx year date day insDinner foodList
    for gunjaData in gunjaDatas:
        sql = "INSERT IGNORE INTO mealGunja(year, date, day, isDinner, foodList) VALUES (%s, %s, %s, %s, %s);"    
        cursor.execute(sql,(gunjaData[4], gunjaData[3], gunjaData[2], gunjaData[0], gunjaData[1]))
    db.commit()
    db.close()

def getGunja(day):
    todayInfo=getDay(day)

    db=getDB()
    cursor = db.cursor()
    sql = "SELECT isDinner, foodList FROM mealGunja WHERE year LIKE %s AND date LIKE %s;"
    cursor.execute(sql,(todayInfo[0],todayInfo[1]))
    rows = cursor.fetchall()

    if len(rows)==0:
        saveGunja()
        cursor.execute(sql,(todayInfo[0],todayInfo[1]))
        rows = cursor.fetchall()
        if len(rows)==0:
            return dayKorean(day) + '에는 식당을 운영하지 않습니다.'
    else:
        lunch = ", ".join(rows[1][1].split(' ')[:3])
        dinner = ", ".join(rows[0][1].split(' ')[:3])
        return dayKorean(day) + '의 점심 메뉴는 ' + lunch + '이고, 저녁 메뉴는 ' + dinner + '입니다.'

def dayKorean(day):
    days = ['B_YESTERDAY', 'YESTERDAY', 'TODAY', 'TOMORROW', 'A_TOMORROW']
    koreans = ['그저께', '어제', '오늘', '내일', '모레']
    return koreans[days.index(day)]

if __name__ == '__main__':
    p(getGunja('B_YESTERDAY'))
    
