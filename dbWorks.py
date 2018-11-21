# -*- coding: utf-8 -*-
import pymysql
import getMeal
from pprint import pprint as p
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
db=getDB()
cursor = db.cursor()
sql = "SELECT * FROM mealGunja"
cursor.execute(sql)
data = cursor.fetchall()
data = list(data)
db.close()
print(data)

song=getMeal.getGunja()
p(song)