import re, requests, bs4
from selenium import webdriver


def getfile(name):
    with open(name, 'r') as f:
        con = f.read()
        f.close()
    return con


def putfile(name, str):
    with open(name, 'w') as f:
        f.write(str)
        f.close()
    return


def mklist(resultes):
    lists = []
    n = 1
    for i in resultes:
        a = (n, f'{i[1]}', f'{i[0]}')
        lists.append(a)
        n = n + 1
    return lists


def showlist(L):
    for i in L:
        out = f'{i[0]}:{i[1]}:{i[2]}'
        print(out)
    return


proxies = {
    'http': 'socks5://127.0.0.1:1080'
}
key = ''
# page = requests.get(key,proxies=proxies)
page = getfile('3.txt')
resulits = re.findall('', page, re.S)
listt = mklist(resulits)

showlist(listt)
k = -1
browser = webdriver.Chrome()

while k != 0:
    k = int(input('which one?'))
    browser.get(listt[k - 1][2])
browser.close()
