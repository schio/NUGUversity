from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pprint import pprint as p
import re
from datetime import datetime
import shortUrlN
def getDriver():
    options = Options()
    #head less mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    #for head less mode detection
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # agent change 
    options.add_argument("lang=ko_KR") 

    # driver setting
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/scio/install/chrome/chromedriver')
    driver.get('http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333')

    # for head less mode detection
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});") #num of plugin spoofing
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

    return driver
def getNotice():
    driver=getDriver()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    numOfTitleSelector = soup.select('body > div > table > tbody > tr > td.index')
    writerSelector = soup.select('body > div > table > tbody > tr > td.writer')
    writeTimeSelector = soup.select('body > div > table > tbody > tr > td.date')
    titleSelector = soup.select('body > div > table > tbody > tr > td.subject > a')
    urlSelector = soup.select('body > div > table > tbody > tr > td.subject > a')
    
    titles=[]
    writeTimes=[]
    writers=[]
    numOfTitles=[]
    urls=[]

    for i in range(len(titleSelector)):
        titles.append(re.sub("†","",titleSelector[i].text.strip()))
        writers.append(writerSelector[i].text.strip())
        writeTimes.append(writeTimeSelector[i].text.strip())
        numOfTitles.append(numOfTitleSelector[i].text.strip())
        urls.append(shortUrlN.create('http://board.sejong.ac.kr/'+str(urlSelector[i].attrs['href'])))#.text.strip()))
        #print('http://board.sejong.ac.kr/'+str(urlSelector[i].attrs['href']))#.text.strip()))
    return titles, writers, writeTimes, numOfTitles, urls


if __name__ == '__main__':
    titles, writers, writeTimes, numOfTitles, urls = getNotice()

    for i in range(len(titles)):
        print(titles[i], writers[i], writeTimes[i], numOfTitles[i], urls[i])