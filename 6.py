from urllib import request,parse

base_url = 'http://www.zznzzn.cn'
path = '/homework/1/index.html'
response = request.urlopen(base_url+path)
print(response.headers,response.code)
print(response.read().decode('utf-8'))
