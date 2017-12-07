from selenium import webdriver
import time,re
import urllib
from urllib import request 
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# chromedriver = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver"   #your chromedriver path 
# driver=webdriver.Chrome(chromedriver)
headers={
	'Host': 'music.163.com',
	'Proxy-Connection': 'keep-alive',
	'Content-Length': '656',
	'Origin': 'http://music.163.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept': '*/*',
	'Referer': 'http://music.163.com/search/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
	'Cookie': '_ntes_nnid=5f937259e913a6da07b4e1fdab40a15c,1503804878746; _ntes_nuid=5f937259e913a6da07b4e1fdab40a15c; vjuids=214711158.15f2d114180.0.c4b876578baf5; vjlast=1508289626.1508289626.30; vinfo_n_f_l_n3=c537a12f07ddb0ab.1.0.1508289674319.0.1508289870476; __csrf=de126f556ec2c3db043e232055786396; __utma=94650624.180416857.1503804890.1512560373.1512623953.45; __utmb=94650624.26.10.1512623953; __utmc=94650624; __utmz=94650624.1505355540.8.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); JSESSIONID-WYYY=MJO%2FDM%5CfNVxZFtxAVIJf%5C734ITFfr6OD9RSw9bhDCd%2FhADSzpiblAUzS6gQ5B8QppiXRh7FfJ29sUuEffYuCE7r76r8lthAsUKyzn6F%5CJwPmupcIPiEQU4n6o418TpZY0AcjxrdONtp2sm6dZMuH8XR4RN5Cy5w3E6jJ4l3R8pdbmnH9%3A1512629232109; _iuqxldmzr_=32'
}

s='小泽直树'
s=urllib.parse.quote(s)


url='http://music.163.com/#/search/m/?s='+s+'&type=1002'



# def execute_times(times):
#     for i in range(times + 1):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(1)
# execute_times(5)
# time.sleep(10)
# content=driver.page_source
# content=driver.find_element_by_tag_name('html').get_attribute('innerHTML')

driver = webdriver.PhantomJS()
driver.get(url)
driver.save_screenshot('1.png')
element=driver.find_element_by_class_name("h-flag")
print(element.text)






# content=driver.page_source

driver.close()