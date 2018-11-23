import os
import sys
import urllib.request
import re
def create(longUrl):
    client_id = "xy0wnnclp1"
    client_secret = "MJPEFw1Bti6ABSZqENaXo2uJ2H8LkFyWyQcTerue"
    encText = urllib.parse.quote(longUrl)
    data = "url=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/util/v1/shorturl"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        shortenUrl=response_body.decode('utf-8')
        return re.sub("\"","",re.findall("http://me2.do/\w*\"",shortenUrl)[0])
    else:
        # print("Error Code:" + rescode)
        return rescode

if __name__ == '__main__':
    url='http://board.sejong.ac.kr/viewcount.do?rtnUrl=/boardview.do?pkid=110237^currentPage=1^searchField=ALL^siteGubun=19^menuGubun=1^bbsConfigFK=333^searchLowItem=ALL&searchValue=&gubun=&tableName=SJU_BBSDATA&fieldName=VIEWCOUNT&viewNum=82&whereCon=PKID=110237'
    short=create(url)
    print(short)