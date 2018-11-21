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
# sql = "SELECT * FROM mealGunja"
# cursor.execute(sql)
# data = cursor.fetchall()
# data = list(data)

# print(data)

gunjaDatas=getMeal.getGunja()
# mealGunja Columns -> idx year date day insDinner foodList

for gunjaData in gunjaDatas:
    sql = "INSERT IGNORE INTO mealGunja(year, date, day, isDinner, foodList) VALUES (%s, %s, %s, %s, %s);"    
    cursor.execute(sql,(gunjaData[4], gunjaData[3], gunjaData[2], gunjaData[0], gunjaData[1]))

# p(gunjaDatas)
# for gunjaData in gunjaDatas:
    # sql = "INSERT IGNORE INTO mealGunja VALUES (NULL, %d, %s, %s, %s, %s)"    
    # print(type(gunjaData[4]), gunjaData[3], gunjaData[2], gunjaData[0], gunjaData[1])
db.commit()
db.close()
