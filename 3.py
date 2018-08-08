import http.cookiejar,urllib.request

filename='1.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
for i in cookie:
    print(i.name+'='+i.value)
