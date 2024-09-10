import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def click_start_button(driver): # WARNING: click_start_button()は副作用があることに注意。button.clickによりページが遷移している。
    try: 
        button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[name='start']")
        button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")

def click_next_button(driver):
    try: 
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-text="NEXT"]')
        next_button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")

def get_question_elements(driver): 
    # driver.implicitly_wait(10)
    question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    return question_elements

def scrape_question_info(driver):
    gray_text = driver.find_element(By.CSS_SELECTOR, ".grayText")
    full_text = gray_text.get_attribute("innerHTML")
    info, ques_num = full_text.split("<br>")
    
    year, ques_num, opt_num = info.split(" ")
    return year, ques_num, opt_num

def scrape_correct_answer(driver):
    kaisetsu_element = driver.find_element(By.CLASS_NAME, "kaisetsu")
    answer_char_element = kaisetsu_element.find_element(By.CLASS_NAME, "answerChar")    
    result = answer_char_element.get_attribute("innerHTML")
    
    if "batu" in result:
        return "誤"
    elif "maru" in result:
        return "正"

def scrape_explanation(driver):
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


def collect_question_data(driver):
    year, ques_num, opt_num = scrape_question_info(driver)
    question_text = scrape_question_text(driver)
    option_text = scrape_option_text(driver)
    answer = scrape_correct_answer(driver)
    kaisetsu = scrape_explanation(driver)
    
    question_data = {
        "year": year,
        "question_number": ques_num,
        "option_number": opt_num,
        "question_text": question_text,
        "option_text": option_text,
        "answer": answer,
        "kaisetsu": kaisetsu
    }
    return question_data

def write_data_to_csv(driver, num_questions, filename='takken_questions.csv'):
    fieldnames = ["year", "question_number", "option_number", "question_text", "option_text", "answer", "kaisetsu"]
    
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file: # windows環境ではnewline=''としておくと安全らしい
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for i in range(num_questions):
            data_dic = collect_question_data(driver)
            writer.writerow(data_dic) 
            
            click_next_button(driver)


def main():
    driver = webdriver.Chrome() 
    driver.implicitly_wait(5)
    driver.get('https://takken-siken.com/marubatu.php')
        
    click_start_button(driver)
    
    write_data_to_csv(driver, num_questions=20, filename="./data/sample.csv")
    
    driver.quit()
    
        
if __name__ == "__main__":
    main()