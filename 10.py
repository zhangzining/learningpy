import requests

s= requests.Session()
s.get('http://httpbin.org/cookies/set/number/1234567890')
response = s.get('http://httpbin.org/cookies')
print(response.text)