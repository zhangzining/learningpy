import requests

res = requests.get('https://github.com/favicon.ico')
print(res.text)
print(res.content)
with open('favicon.ico','wb') as f:
    f.write(res.content)
    f.close()

files = {
    'file':open('favicon.ico','rb')
}
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)