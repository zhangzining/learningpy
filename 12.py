import requests
from requests.exceptions import ReadTimeout,MissingSchema

proxies={
    'http':'socks5://127.0.0.1:1080'
}
while True:
    try:
        key=input('please input what you want to test')
        response = requests.get(key,proxies=proxies)
        print(response.status_code)
    except MissingSchema:
        key = f'http://{key}'
        response = requests.get(key, proxies=proxies)
        print(response.status_code)
    except ReadTimeout:
        print('time out')