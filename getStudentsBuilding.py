from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pprint import pprint as p
import re
from datetime import datetime
import getMeal

def saveMenu():
    driver=getMeal.getDriver()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    menu=[]
    price=[]

    menus = soup.select('body > div > div.body > div > div > div > div.tab-content > div > div > div.article > div > table > tbody > tr > th > div.th')
    for m in menus:
        menu.append(m.text.strip())

    prices = soup.select('body > div > div.body > div > div > div > div.tab-content > div > div > div.article > div > table > tbody > tr > td > div')
    for pr in prices:
        price.append(pr.text.strip())
    
if __name__ == '__main__':
    saveMenu()