from selenium import webdriver
import time,re
import urllib
from urllib import request 
import urllib.request

#line 10, line 12, line 57 should be changed


urltoken="wkzstc"    #your zhihu personal infomation page token

chromedriver = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver"   #your chromedriver path 
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

	url="https://www.zhihu.com/people/"+urltoken+"/followers?page="+str(j)   
	driver.get(url)

	execute_times(1)

	content=driver.page_source

	resLink = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
	links = re.findall(resLink,content,re.I|re.S|re.M)

	for i in range(0, len(links), 2):
		if(links[i].startswith('/people') and (not links[i].startswith('/people/wkzstc/'))):
			results.append("https://www.zhihu.com"+links[i])

for value in results:
	with open("links.txt","a",encoding='gb18030') as f:
		f.write(value+'\n')

urls=[]
f = open("links.txt","r")      #you can split links.txt to several files in case you request too many times that zhihu forbids you for a while.       
lines = f.readlines()             
for line in lines  :               
	urls.append(line[0:len(line)-1])
f.close()


headers={
	'Cookie':'' #your login cookie, otherwise there will be some data remains unknown
}

with open("result.txt","a",encoding='gb18030') as f:
		f.write("昵称\t签名\t性别\t回答\t提问\t文章\t专栏\t想法\t被赞同\t被感谢\t被收藏\t参与公共编辑\t关注了\t关注者\t赞助的live\t关注的话题\t关注的专栏\t关注的问题\t关注的收藏夹\n")

usecookie=False
i=0

while i<len(urls):
	url=urls[i]

	if(usecookie):
		req = request.Request(url=url,headers=headers)
		response = request.urlopen(req)
		content=response.read().decode('utf-8')
		usecookie=False
	else:
		response = urllib.request.urlopen(url)
		content=response.read().decode('utf-8')

	s=""

	resName = r'<h1 class="ProfileHeader-title".*?><span.*?>(.*?)</span>.*?</h1>' 
	name =  re.findall(resName, content, re.S|re.M)  
	try:
		name=name[0]
		s=s+name+"\t"

		resHeadLine= r'<h1 class="ProfileHeader-title".*?><span class="RichText ProfileHeader-headline".*?>(.*?)</span>.*?</h1>' 
		headline=re.findall(resHeadLine, content, re.S|re.M)  
		headline=headline[0]
		if(headline==''):
			headline='null'
		s=s+headline+"\t"


		resGender='"Icon Icon--male"'
		gender=re.search(resGender, content,re.S|re.M)
		if(gender!=None):
			gender='male'
		else:
			resGender='"Icon Icon--female"'
			gender=re.search(resGender, content,re.S|re.M)
			if(gender!=None):
				gender='female'
			else:
				gender='unknown'
		s=s+gender+"\t"

		resAnswer=r'<span class="Tabs-meta".*?>(.*?)</span>'
		answer=re.findall(resAnswer, content, re.S|re.M)
		answerNumber=answer[0]
		questionNumber=answer[1]
		articleNumber=answer[2]
		columnNumber=answer[3]
		thinkingNumber=answer[4]
		s=s+answerNumber+"\t"+questionNumber+"\t"+articleNumber+"\t"+columnNumber+"\t"+thinkingNumber+"\t"

		resDiv=r'<div class="Profile-sideColumnItem".*?>(.*?)</div>'
		number=re.findall(resDiv,content,re.S|re.M)
		if(len(number)!=3 and len(number)!=4):
			resAgree=r'<div class="IconGraf".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></div>'
			agree=re.findall(resAgree, content, re.S|re.M)
			try:
				agree=agree[0]
			except:
				agree='0'

			resThanks=r'<div class="Profile-sideColumnItemValue".*?><!-- react-text.*?>(.*?)<!-- /react-text -->'
			thanks=re.findall(resThanks, content, re.S|re.M)
			try:
				thanks = re.sub("\D", "", thanks[0])
			except:
				thanks='0'		

			resCollect=r'<div class="Profile-sideColumnItemValue".*?><!-- react-text.*?>.*?<!-- /react-text --><!-- react-text.*?>.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text --></div>'
			collect=re.findall(resCollect, content, re.S|re.M)
			try:
				collect= re.sub("\D", "", collect[0])
			except:
				collect='0'

			resEdit=r'<a class="Profile-sideColumnItemLink".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></a>'
			edit=re.findall(resEdit, content, re.S|re.M)
			try:
				edit=edit[0]
			except:
				resEdit=r'<span class="Profile-sideColumnItemLink".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></span>'
				edit=re.findall(resEdit, content, re.S|re.M)
				try:
					edit=edit[0]
				except:
					edit=0
		elif(len(number)==3):
			resAgree=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></div></div>'
			agree=re.findall(resAgree, content, re.S|re.M)
			agree=agree[0]

			resThanks=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><div class="Profile-sideColumnItemValue".*?><!-- react-text.*?>(.*?)<!-- /react-text -->'
			thanks=re.findall(resThanks, content, re.S|re.M)
			try:
				thanks = re.sub("\D", "", thanks[0])
			except:
				thanks=0

			resCollect=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><div class="Profile-sideColumnItemValue".*?><!-- react-text.*?>.*?<!-- /react-text --><!-- react-text.*?>.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text --></div>'
			collect=re.findall(resCollect, content, re.S|re.M)
			try:
				collect= re.sub("\D", "", collect[0])
			except:
				collect=0

			resEdit=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><a class="Profile-sideColumnItemLink".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></a>'
			edit=re.findall(resEdit, content, re.S|re.M)
			try:
				edit=edit[0]
			except:
				resEdit=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><span class="Profile-sideColumnItemLink".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></span>'
				edit=re.findall(resEdit, content, re.S|re.M)
				edit=edit[0]

		elif(len(number)==4):
			resAgree=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></div></div>'
			agree=re.findall(resAgree, content, re.S|re.M)
			agree=agree[0]

			resThanks=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><div class="Profile-sideColumnItemValue".*?><!-- react-text.*?>(.*?)<!-- /react-text -->'
			thanks=re.findall(resThanks, content, re.S|re.M)
			try:
				thanks = re.sub("\D", "", thanks[0])
			except:
				thanks=0

			resCollect=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><div class="Profile-sideColumnItemValue".*?><!-- react-text.*?>.*?<!-- /react-text --><!-- react-text.*?>.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text --></div>'
			collect=re.findall(resCollect, content, re.S|re.M)
			try:
				collect= re.sub("\D", "", collect[0])
			except:
				collect=0

			resEdit=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><a class="Profile-sideColumnItemLink".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></a>'
			edit=re.findall(resEdit, content, re.S|re.M)
			try:
				edit=edit[0]
			except:
				resEdit=r'<div class="Profile-sideColumnItems".*?><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?>.*?</div><div class="Profile-sideColumnItem".*?><span class="Profile-sideColumnItemLink".*?<!-- react-text.*?<!-- /react-text --><!-- react-text.*?>(.*?)<!-- /react-text -->.*?<!-- /react-text --></span>'
				edit=re.findall(resEdit, content, re.S|re.M)
				edit=edit[0]
		if collect>100000000000:
			collect=0
		s=s+str(agree)+'\t'+str(thanks)+'\t'+str(collect)+'\t'+str(edit)+'\t'

		resNumber=r'<div class="NumberBoard-value".*?>(.*?)</div>'
		number=re.findall(resNumber, content, re.S|re.M)
		try:
			numberOfWatching=number[0]
		except:
			numberOfWatching='unknown'
		try:
			numberOfFans=number[1]
		except:
			numberOfFans='unknown'
		s=s+numberOfWatching+"\t"+numberOfFans+"\t" 


		resOther=r'<span class="Profile-lightItemValue".*?>(.*?)</span>'
		other=re.findall(resOther, content, re.S|re.M)
		try:
			if(len(other)==5):
				numberOfLive=other[0]
				numberOfTopics=other[1]
				numberOfColumns=other[2]
				numberOfQuestions=other[3]
				numberOfCollect=other[4]		
			else:
				numberOfLive='0'
				numberOfTopics=other[0]
				numberOfColumns=other[1]
				numberOfQuestions=other[2]
				numberOfCollect=other[3]
		except:
			usecookie=True
			continue
		s=s+numberOfLive+"\t"+numberOfTopics+"\t"+numberOfColumns+"\t"+numberOfQuestions+"\t"+numberOfCollect+"\n"
	except:
		s=url+"\n"
	with open("result.txt","a",encoding='gb18030') as f: 
		f.write(s)
	i=i+1
	print('finish No.'+str(i)+' '+url)
	time.sleep(1)

