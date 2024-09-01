
import requests, bs4


def scrape_question(soup):
    question_section = soup.find('section', class_='content mondai')
    
    question_number = question_section.find('h3').get_text().strip('問')
    
    question = "次の1から4までの記述のうち、民法の規定、判例及び下記判決文によれば、誤っているものはどれか。"
    # number = "1"
    return question, question_number 

def main():
    res = requests.get('https://takken-siken.com/kakomon/2023/01.html')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    
    # question_section = soup.find('section', class_='content mondai')
    # if question_section:
    #     question_text = question_section.get_text(strip=True)
    #     print(question_text)
    # else:
    #     print("couldnt find question section")
        
    # print(question_section.find('h3'))
    
        # 問題番号を含むh3タグを取得
    ques_num_element = soup.find('h3')
    ques_num = ques_num_element.get_text(strip=True)
    
    # 問題番号と問題文を分離
    number = ques_num.replace('問', '').strip()  # "問1" から "1" を抽出
    # question = ques_num_element.find_next('div', class_='content mondai').get_text(strip=True).replace(ques_num, '').strip()
    
    # print(question)
    print(number)

if __name__ == "__main__":
    main()