from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pprint import pprint as p
import re
from datetime import datetime

def getDriver(url):
    options = Options()
    #head less mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    #for head less mode detection
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # agent change 
    options.add_argument("lang=ko_KR") 

    # driver setting
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/scio/install/chrome/chromedriver')
    driver.get(url)

    # for head less mode detection
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});") #num of plugin spoofing
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

    return driver

def getUrl(room):
    # A B C D 3층
    if room=='A':
        return ['http://210.107.226.14/seat/roomview5.asp?room_no=1']
    elif room=='B':
        return ['http://210.107.226.14/seat/roomview5.asp?room_no=2']
    elif room=='C':
        return ['http://210.107.226.14/seat/roomview5.asp?room_no=3']
    elif room=='D':
        return ['http://210.107.226.14/seat/roomview5.asp?room_no=4','http://210.107.226.14/seat/roomview5.asp?room_no=5']
    elif room=='3층':
        return ['http://210.107.226.14/seat/roomview5.asp?room_no=6','http://210.107.226.14/seat/roomview5.asp?room_no=7']

def getEmptySeats(room):
    urls=getUrl(room)
    info=[]
    totalSeats=0
    emptySeats=0
    for i in range(len(urls)):
        info.append([])
        driver=getDriver(urls[i])
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        seatsInfo = soup.select('body > center > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > font > b')
        for n in seatsInfo:
            info[i].append(n.text.strip())
    
    for _info in info:
        totalSeats = totalSeats + int(_info[2])
        emptySeats = emptySeats + int(_info[6])
    room=room+'열람실'
    return room + '의 총 좌석수는 ' + str(totalSeats) + ' 잔여좌석수는 ' + str(emptySeats) + '입니다.'

if __name__ == '__main__':
    info=getEmptySeats('3층')
    p(info)