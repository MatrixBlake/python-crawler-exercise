from selenium import webdriver
import time,re
import urllib
from urllib import request 
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from urllib import request





urls=[]
f = open("link.txt","r")             
lines = f.readlines()             
for line in lines  : 
	if(line[0:len(line)-1] != ""):            
		urls.append(line[0:len(line)-1])
f.close()

print(urls)



for i in range(0,1764):  //会被微博强行断连接，下次重来时候修改初始值。1764是link的总数量
	request.urlretrieve(urls[i], "images/"+str(i)+".jpg")
	if i%10 == 0:
		print(i)

