from selenium import webdriver
import time,re
import urllib

urltoken="wkzstc"

chromedriver = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver"  
driver=webdriver.Chrome(chromedriver)
results=[]

url="https://www.zhihu.com/people/"+urltoken+"/followers"
driver.get(url)
def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
execute_times(1)
content=driver.page_source
res=r'<button class="Button PaginationButton Button--plain".*?><!-- react-text.*?>(.*?)<!-- /react-text --></button>'
numbers = re.findall(res,content,re.I|re.S|re.M)
lastpage=int(numbers[len(numbers)-1])

for j in range(1,(lastpage+1)):

	url="https://www.zhihu.com/people/wkzstc/followers?page="+str(j)
	driver.get(url)

	execute_times(1)

	content=driver.page_source

	# resName = r'<div class="ContentItem-head".*?><a class="UserLink.*?>(.*?)</a></div>'  
	# names =  re.findall(resName, content, re.S|re.M)  

	resLink = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
	links = re.findall(resLink,content,re.I|re.S|re.M)

	for i in range(0, len(links), 2):
		if(links[i].startswith('/people') and (not links[i].startswith('/people/wkzstc/'))):
			results.append("https://www.zhihu.com/"+links[i])

for value in results:
	print(value)

