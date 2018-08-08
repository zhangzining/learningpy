import requests
import urllib
response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(response.headers)
print(response.text)
print(response.cookies)
response = urllib.request.urlopen('http://www.zznzzn.cn')
with open('2.txt','w') as f:
    f.write(response.read().decode('utf-8'))
    f.close

