from bs4 import BeautifulSoup
import re


html=''
with open('2.txt','r') as f:
    html = f.read()
    f.close()

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.head.meta)