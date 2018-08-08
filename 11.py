import requests
import urllib3
url = 'https://www.12306.cn'
try:
    urllib3.disable_warnings()
    response = requests.get(url,verify=False)
    print(response.status_code)

except requests.excptions.SSLError as e:
    print(e.reason)