
import requests, bs4


def scrape_question(soup):
    question_section = soup.find('section', class_='content mondai')
    
    question_number = question_section.find('h3').get_text()
    # print(question_number)
    question = question_section.get_text().strip(question_number).strip()
    question_number = question_number.strip('問')
    
    return question, question_number 

def main():
    res = requests.get('https://takken-siken.com/kakomon/2023/01.html')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    
    question, number = scrape_question(soup)
    print(question)
    print(number)
    

if __name__ == "__main__":
    main()