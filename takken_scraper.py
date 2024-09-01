
import requests, bs4
import re


def scrape_question(soup):
    question_section = soup.find('section', class_='content mondai')
    
    question_number = question_section.find('h3').get_text()
    question = question_section.get_text().strip(question_number).strip()
    question_number = question_number.strip('問')
    
    return question, question_number 

def scrape_year(soup): # NOTE: URLから年度を取得するようにしても良いかも
    year_text = soup.find('h2').get_text()
    match = re.search(r'(令和|平成)\d+年', year_text) # NOTE: 平成と令和以外対応していないので注意
    if match:
        return match.group(0)
    return None

def scrape_category(soup):
    return "1 - 権利関係", "hoge"

def main():
    res = requests.get('https://takken-siken.com/kakomon/2023/01.html')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    
    question, number = scrape_question(soup)
    
    print(f'{question = }')
    print(f'{number = }')
    

if __name__ == "__main__":
    main()