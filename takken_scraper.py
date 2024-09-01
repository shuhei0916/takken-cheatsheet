
import requests, bs4


def scrape_question(soup):
    question = "次の1から4までの記述のうち、民法の規定、判例及び下記判決文によれば、誤っているものはどれか。"
    number = "1"
    return question, number 

def main():
    # html = 
    res = requests.get('https://takken-siken.com/kakomon/2023/01.html')
    res.raise_for_status()
    # print(type(res))

    # print(res.text)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    
    
    question_section = soup.find('section', class_='content mondai')
    if question_section:
        question_text = question_section.get_text(strip=True)
        print(question_text)
    else:
        print("couldnt find question section")
    # print(type(soup))
    # hoge = soup.select('div')
    # print(hoge)

    # hehe = soup.select('#gbqfbb')
    # print('hehe', hehe)

    # with open('./sample-html.html') as f:
    #     print(type(f))
    #     example_soup = bs4.BeautifulSoup(f, features="html.parser")
    #     elems = example_soup.select('#author')
    #     print(type(elems))
    #     print(elems[0])
    #     print(elems[0].getText())

if __name__ == "__main__":
    main()