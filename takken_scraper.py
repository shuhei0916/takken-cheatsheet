
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
    return "不正解"

def scrape_question(driver):
    pass


def main():
    driver = webdriver.Chrome() 
    driver.get('https://takken-siken.com/marubatu.php')
        
    button_click(driver)
    
    question_elements = find_question_elements(driver)
    print(type(driver))
    print(type(question_elements))
    
    # # if not question_elements:
    # #     print("question_element not found")
    # for i, element in enumerate(question_elements):
    #     print(i)
    #     # print(i, ": ", element.text)
    #     html = element.get_attribute("innerHTML")
    #     print(html)
    #     # print(type(element))
    #     # print
        
    hoge = driver.find_element(By.CSS_SELECTOR, "section.content h3")
    print(hoge.text)
    # hoge.find_element()
    
    driver.quit()
        

if __name__ == "__main__":
    main()