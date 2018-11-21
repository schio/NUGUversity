from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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

seqLen=10
# data[10][4]

data=[]
# notices = soup.select('tr.seq-07 > th > div.th') #[0] 목(11/22) [1] 중식
# notices = soup.select('tr.seq-07 > td > div.td')
# # print(notices)
# for n in notices:
#     print(n.text.strip())
for i in range(seqLen):
    if i !=9:
        if (i+1)%2==1:
            data.append([])
            notices = soup.select('tr.seq-0' + str(i+1) + ' > th > div.th')
            temp=[]
            for n in notices:
                temp.append(n.text.strip())
            data[i].append(temp[0]) #date,day
            data[i].append(temp[1]) #isDinner
            # print(i)
            # notices = soup.select('tr.seq-0'+str(i+1)+' > td > div')
            # temp[0]=str('')
            # for n in notices:
            #     temp[0]=temp+n+' '
        else:
            data.append([])
            notices = soup.select('tr.seq-0' + str(i+1) + ' > th > div.th')
            temp=[]
            for n in notices:
                temp.append(n.text.strip())

            t=i-1
            data[i].append(data[i-1][0]) #date,day
            data[i].append(temp[0]) #isDinner

print(data)

# print(soup)

# get html
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = soup.select('div.card-body > div.card-title')
# for n in notices:
#     print(n.text.strip())
driver.quit()