import requests,re

listID1='105903649'
listID2='105903649'

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

r1 = requests.get("http://music.163.com/playlist?id="+listID1, headers=headers)
content1=r1.text


r2 = requests.get("http://music.163.com/playlist?id="+listID2, headers=headers)
content2=r2.text

resName=r'<li><a href="/song\?id=.*?>(.*?)</a></li>'
names1 = re.findall(resName,content1,re.I|re.S|re.M)
names2 = re.findall(resName,content2,re.I|re.S|re.M)

total=len(names1)+len(names2)
same=0
for i in range(0,len(names1)):
	for j in range(0,len(names2)):
		if(names1[i]==names2[j]):
			same=same+1
			total=total-1
			break
similarity=round(same/total*100,2)
print('List1 has '+str(len(names1))+' songs')
print('List2 has '+str(len(names2))+' songs')
print('There are '+str(same)+' same songs')
print('Your similarity is '+str(similarity)+'%')
print('The same songs show '+str(round(same/len(names1)*100,2))+'%'+' in list1')
print('The same songs show '+str(round(same/len(names2)*100,2))+'%'+' in list2')


