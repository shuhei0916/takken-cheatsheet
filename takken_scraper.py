import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def start_button_click(driver): # WARNING: start_button_click()は副作用があることに注意。button.clickによりページが遷移している。
    try: 
        button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[name='start']")
        button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")

def next_button_click(driver):
    next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-text="NEXT"]')
    next_button.click()

def find_question_elements(driver): 
    # driver.implicitly_wait(10)
    question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    return question_elements

def scrape_info(driver):
    gray_text = driver.find_element(By.CSS_SELECTOR, ".grayText")
    full_text = gray_text.get_attribute("innerHTML")
    info, ques_num = full_text.split("<br>")
    
    year, ques_num, opt_num = info.split(" ")
    return year, ques_num, opt_num

def scrape_answer(driver):
    kaisetsu_element = driver.find_element(By.CLASS_NAME, "kaisetsu")
    answer_char_element = kaisetsu_element.find_element(By.CLASS_NAME, "answerChar")    
    result = answer_char_element.get_attribute("innerHTML")
    
    if "batu" in result:
        return "誤"
    elif "maru" in result:
        return "正"

def scrape_kaisetsu(driver):
    kaisetsu_element = driver.find_element(By.CLASS_NAME, "kaisetsu")
    kaisetsu = kaisetsu_element.find_element(By.CSS_SELECTOR, "div")
    kaisetsu_text = kaisetsu.get_attribute("innerText") # NOTE: kaisetsu.textでは取得できない(is_displayed() == Falseのため)
    return kaisetsu_text

def scrape_option_text(driver):
    option_element = driver.find_element(By.XPATH, "//section[@class='content']/div/b")
    option_text = option_element.text
    return option_text

def scrape_question_text(driver):
    question_element = driver.find_element(By.XPATH, "//section[@class='content']/div")
    option_text = scrape_option_text(driver)
    question_text = question_element.text.strip(option_text).strip()
    return question_text


def collect_scraping_data(driver):
        #     # 各問題のデータを取得し、即座にCSVに書き込む
    #     for i in range(num_questions):
    #         # データをスクレイピング
    #         year, ques_num, opt_num = extract_question_info(driver)
    #         question_text = scrape_question_text(driver)
    #         option_text = scrape_option_text(driver)
    #         answer = scrape_answer(driver)
    #         kaisetsu = scrape_kaisetsu(driver)
            
    #         # データを辞書形式にする
    #         question_data = {
    #             "year": year,
    #             "question_number": ques_num,
    #             "option_number": opt_num,
    #             "question_text": question_text,
    #             "option_text": option_text,
    #             "answer": answer,
    #             "kaisetsu": kaisetsu
    #         }
            
    #         # データを即座にCSVに書き込む
    #         writer.writerow(question_data)
    pass

def write_data_to_csv(driver, num_questions, filename='takken_questions.csv'):
    # フィールド名を定義
    fieldnames = ["year", "question_number", "option_number", "question_text", "option_text", "answer", "kaisetsu"]
    
    # CSVファイルをオープン（書き込みモード）
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # ヘッダーを書き込む
        writer.writeheader()
        


        # 次の問題に進むための処理（ボタンをクリックするなど）
        # button_click(driver) など、次の問題に遷移するためのコードを追加


def main():
    # driver = webdriver.Chrome() 
    # driver.get('https://takken-siken.com/marubatu.php')
        
    # start_button_click(driver)
    
    # driver.quit()
    
    write_data_to_csv("hoge", "hoge", filename="./data/sample.csv")
    
        

if __name__ == "__main__":
    main()