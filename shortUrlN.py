import os
import sys
import urllib.request

def create():
    client_id = "xy0wnnclp1"
    client_secret = "MJPEFw1Bti6ABSZqENaXo2uJ2H8LkFyWyQcTerue"
    encText = urllib.parse.quote("https://developers.naver.com/docs/utils/shortenurl")
    data = "url=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/util/v1/shorturl"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        return rescode