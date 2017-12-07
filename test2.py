import requests

url='http://music.163.com/weapi/cloudsearch/get/web?csrf_token=de126f556ec2c3db043e232055786396'

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

data={'params':'iqpesAQ1mJTF8sN6UOYLVB4JTKnPChawIef0dAPpFJ0utsa9o+oA4upNhYmf3XfDSf4rnhlnwvXCFqneTRfeaTQPQZEv+vEz5YKyxFuipzMT+N1Ln2dSsTtp7Jrp8jPBKUe+VNB8oSP/Do0+vissBjyPpoVYVwiwdEihLKrsToZu3MyNqcrrKGEvdChhooBs11v1BlWhjjnDi6rQoL+w12U3fPfau2DN7WMgP6E7G5/VpFN8a4n7lPl/rklyOkQKNZt0miSwkWfwjdFgIwp+r+YluehQ7rKyjy/WKaIE0sfh+C2SKja3qxdR+Ce/3gr8Gv8LYBJj7tiBdT6iviUNWtHYp2TwMzPdA5vZu/3NI1Q=',
'encSecKey':'546553818dc4b6a6a58805758273404b772df199f6a09937246295e3133a1f58b307ff883a708150164ac41a57e239c68e61b20ee9e0f2fa04a4805113990473fc7a045b10ba6ed97b9c2e82b4f8347b2e17920a2793bdf76379e8bb70ea87179cb041951f4fed029e710202332b2f79622101821dcba699ae682fd38a871849'}
r = requests.post(url,data=data)
print(r.text)

