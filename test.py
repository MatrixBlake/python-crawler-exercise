import urllib.parse
import requests,re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

s='小泽直树'
s=urllib.parse.quote(s)


url1='http://music.163.com/#/search/m/?s='+s
print(url1)
url2='http://music.163.com/#/playlist?id=105903649'


headers={
	'Host': 'music.163.com',
	'Proxy-Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Referer': 'http://music.163.com/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
}


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=['--ssl-protocol=any'])


# desired_capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
# driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities,service_args=['--ssl-protocol=any'])
driver.get(url1)
print(driver.page_source)