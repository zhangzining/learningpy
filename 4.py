from urllib import request,error

try:
    response = request.urlopen('http://www.zznzzn.cn/dsfadf.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('successed')