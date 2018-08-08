import requests

re = requests.get('http://httpbin.org/user-agent')
print(re.text)
header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}
re = requests.get('http://httpbin.org/user-agent',headers=header)
print(re.text)
data = {
    'name':'asdfas',
    'age':12
}
re = requests.get('http://httpbin.org/get',params=data)
print(re.text)