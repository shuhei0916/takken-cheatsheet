
import requests, bs4

res = requests.get('https://www.google.com/')
res.raise_for_status()
print(type(res))

# print(res.text)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
hoge = soup.select('div')
print(hoge)

hehe = soup.select('#gbqfbb')
print('hehe', hehe)