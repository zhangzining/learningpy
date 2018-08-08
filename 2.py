import urllib.request

proxy_hander = urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:1081',
    'https':'https://127.0.0.1:1082',
    'socks5':'127.0.0.1:1080'
})
opener = urllib.request.build_opener(proxy_hander)
response = opener.open('http://www.baidu.com')
print(response.read())