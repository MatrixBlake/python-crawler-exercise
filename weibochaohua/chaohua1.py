from selenium import webdriver
import time,re
import urllib
from urllib import request 
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains



chromedriver = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver"  
driver=webdriver.Chrome(chromedriver)
results=[]

url="https://m.weibo.cn/p/index?containerid=100808ef790ff5e3d30b4a0a579ffc7b36ae35&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%BE%90%E6%A2%A6%E6%B4%81&featurecode=20000320"
driver.get(url)
time.sleep(3)

driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/div/ul/li[2]/span").click()
# ActionChains(driver).context_click().send_keys('N').perform() 

def execute_times(times):
    for i in range(times):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
        time.sleep(3)       
execute_times(45) //根据实际情况修改
content=driver.page_source


res=r'<div class=\"m-img-box m-imghold-square\"><img src="(.*?)" />.*?</div>'
imgs = re.findall(res,content,re.I|re.S|re.M)

print(imgs)



for img in imgs:
	with open("links.txt","a",encoding='gb18030') as f:
		f.write(img+'\n')





