
import requests, bs4
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_question(driver): 
    driver.implicitly_wait(10)
    question_elements = driver.find_elements(By.CSS_SELECTOR, "section.content")
    return question_elements

def main():
    driver = webdriver.Chrome() 

    driver.get('https://takken-siken.com/marubatu.php')
    
    # page_source = driver.page_source
    # print(page_source)
    
    # # JavaScriptで直接要素を取得
    # question_text = driver.execute_script("return document.querySelector('section.content').innerText;")
    # print(question_text)
    
    main_contents = driver.find_elements(By.ID, "main_contents")
    if not main_contents:
        print("main_contents not found")
    for element in main_contents:
        print(element.text)
    
    # question_elements = scrape_question(driver)
    # if not question_elements:
    #     print("要素が見つかりませんでした。")
    # for element in question_elements:
    #     print(element.text)
        
    driver.quit()
        

if __name__ == "__main__":
    main()