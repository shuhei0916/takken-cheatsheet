
import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def button_click(driver): # WARNING: button_click()は副作用があることに注意。button.clickによりページが遷移している。
    try: 
        button = driver.find_element(By.CSS_SELECTOR, "button.submit.sendConfigform.hover[name='start']")
        button.click()
    except Exception as e:
        print(f"エラーが発生しました:{e}")

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

def scrape_kaisetsu(self):
    return "誤り。令和4年(2022年)4月1日に成年年齢が18歳に引き下げられました。"

def scrape_question(driver):
    pass


def main():
    driver = webdriver.Chrome() 
    driver.get('https://takken-siken.com/marubatu.php')
        
    button_click(driver)



    driver.quit()
        

if __name__ == "__main__":
    main()