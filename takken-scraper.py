
import requests, bs4


# html = 
res = requests.get('https://www.google.com/')
res.raise_for_status()
print(type(res))

# print(res.text)
# soup = bs4.BeautifulSoup(res.text, features="html.parser")
# hoge = soup.select('div')
# print(hoge)

# hehe = soup.select('#gbqfbb')
# print('hehe', hehe)

with open('./sample-html.html') as f:
    print(type(f))
    example_soup = bs4.BeautifulSoup(f, features="html.parser")
    elems = example_soup.select('#author')
    print(type(elems))
    print(elems[0])
    print(elems[0].getText())