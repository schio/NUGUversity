from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pprint import pprint as p
import re

options = Options()
#head less mode
options.add_argument('--headless')
options.add_argument('--no-sandbox')

#for head less mode detection
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # agent change 
options.add_argument("lang=ko_KR") 

# driver setting
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/scio/install/chrome/chromedriver')
# driver.get('https://bds.bablabs.com/restaurants/MTI1NTM3Ng%3D%3D?campus_id=7u7tS3d3EL')
driver.get('http://m.sejong.ac.kr/front/cafeteria.do')

# for head less mode detection
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});") #num of plugin spoofing
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

# driver.implicitly_wait(3)
# driver.get_screenshot_as_file('test1.png')

#군자관 메뉴 클릭
driver.find_element_by_xpath("//a[contains(@onclick,'selectedCafeteria(3);')]").click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data=[]
for i in range(10): #월화수목금x중식,석식 = 10
    if i !=9:
        if (i+1)%2==1: #seq가 홀수면 날짜, 석식 여부가 나오지만 짝수일 경우 석식 여부만 나와서
            data.append([])

            # 요일, 날짜, 석식여부 크롤링
            dateAndIsDinner = soup.select('tr.seq-0' + str(i+1) + ' > th > div.th')
            temp=[]
            for n in dateAndIsDinner:
                temp.append(n.text.strip())
            data[i].append(temp[0]) #date,day
            data[i].append(temp[1]) #isDinner

            # 메뉴리스트 크롤링
            menu = soup.select('tr.seq-0'+str(i+1)+' > td > div')
            temp[0]=''
            for n in menu:
                temp[0]=temp[0]+str(n.text.strip())+' '
            data[i].append(temp[0])

            # day, date 전처리
            day=str(re.split("\(",data[i][0])[0])+'요일'
            date=str(re.split("\(",data[i][0])[1])
            date=str(re.sub("/","월",date))
            date=str(re.sub("\)","일",date))
            data[i].append(day)
            data[i].append(date)

            #메뉴 데이터 클리닝
            data[i][2]=re.sub("&S","",data[i][2])
            data[i][2]=re.sub(" ","",data[i][2])
            data[i][2]=re.sub("\\n"," ",data[i][2])
            data[i][2]=re.sub("/"," ",data[i][2])
        else:
            data.append([])

            # 요일, 날짜, 석식여부 크롤링
            dateAndIsDinner = soup.select('tr.seq-0' + str(i+1) + ' > th > div.th')
            temp=[]
            for n in dateAndIsDinner:
                temp.append(n.text.strip())
            data[i].append(data[i-1][0]) #date,day
            data[i].append(temp[0]) #isDinner

            # 메뉴리스트 크롤링
            menu = soup.select('tr.seq-0'+str(i+1)+' > td > div')
            temp[0]=''
            for n in menu:
                temp[0]=temp[0]+str(n.text.strip())+' '
            data[i].append(temp[0])

            # day, date 전처리
            day=str(re.split("\(",data[i][0])[0])+'요일'
            date=str(re.split("\(",data[i][0])[1])
            date=str(re.sub("/","월",date))
            date=str(re.sub("\)","일",date))
            data[i].append(day)
            data[i].append(date)

            #메뉴 데이터 클리닝
            data[i][2]=re.sub("&S","",data[i][2])
            data[i][2]=re.sub(" ","",data[i][2])
            data[i][2]=re.sub("\\n"," ",data[i][2])
            data[i][2]=re.sub("/"," ",data[i][2])
    elif i==9:
        data.append([])
        # 요일, 날짜, 석식여부 크롤링
        dateAndIsDinner = soup.select('tr.seq-10 > th > div.th')
        temp=[]
        for n in dateAndIsDinner:
            temp.append(n.text.strip())
        data[9].append(data[8][0]) #date,day
        data[9].append(temp[0]) #isDinner

        # 메뉴리스트 크롤링
        menu = soup.select('tr.seq-10 > td > div')
        temp[0]=''
        for n in menu:
            temp[0]=temp[0]+str(n.text.strip())+' '
        data[9].append(temp[0])

        # day, date 전처리
        day=str(re.split("\(",data[i][0])[0])+'요일'
        date=str(re.split("\(",data[i][0])[1])
        date=str(re.sub("/","월",date))
        date=str(re.sub("\)","일",date))
        data[i].append(day)
        data[i].append(date)

        #메뉴 데이터 클리닝
        data[i][2]=re.sub("&S","",data[i][2])
        data[i][2]=re.sub(" ","",data[i][2])
        data[i][2]=re.sub("\\n"," ",data[i][2])
        data[i][2]=re.sub("/"," ",data[i][2])


for row in data:
    del row[0]
# p(data)

driver.quit()